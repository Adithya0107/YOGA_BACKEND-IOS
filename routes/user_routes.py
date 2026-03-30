from flask import Blueprint, request, jsonify
from models.user_model import (
    create_user, get_user_by_email, get_all_users, 
    update_user_profile, change_user_password,
    add_user_progress, get_user_progress_history,
    get_user_stats, get_user_activity,
    store_otp, verify_otp, delete_otp,
    reset_password_by_email, generate_daily_plan
)
from db_config import get_db_connection
from email_config import send_otp_email, send_password_reset_email
import random
import re
from datetime import datetime, timedelta

user_bp = Blueprint("user_bp", __name__)


# ============================================================
# Password Validation Helper
# ============================================================

def validate_password(password):
    """
    Validate password strength. Returns (is_valid, error_message).
    Requirements:
    - Exactly 8 characters long (as requested)
    - At least 1 uppercase letter (A-Z)
    - At least 1 lowercase letter (a-z)
    - At least 1 digit (0-9)
    - At least 1 special character (!@#$%^&* etc.)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    errors = []
    
    if not re.search(r'[A-Z]', password):
        errors.append("1 uppercase letter (A-Z)")
    if not re.search(r'[a-z]', password):
        errors.append("1 lowercase letter (a-z)")
    if not re.search(r'[0-9]', password):
        errors.append("1 number (0-9)")
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?`~]', password):
        errors.append("1 special character (!@#$%^&*)")
    
    if errors:
        suggestion = "Password must contain: " + ", ".join(errors)
        return False, suggestion
    
    return True, ""


def generate_otp():
    """Generate a random 6-digit OTP."""
    return str(random.randint(100000, 999999))


# ============================================================
# Send OTP (for sign-up)
# ============================================================

@user_bp.route("/send_signup_otp", methods=["POST"])
def send_signup_otp():
    data = request.json
    email = data.get("email", "").strip()

    if not email:
        return jsonify({"message": "Please enter a valid email address."}), 400

    # Basic email format validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"message": "Please enter a valid email address."}), 400

    # Task 1: Enforce small letters only for email
    if any(char.isupper() for char in email):
        return jsonify({"message": "Please enter email in lowercase letters only."}), 400

    # Check if user already exists
    existing = get_user_by_email(email)
    if existing:
        return jsonify({"message": "An account with this email already exists. Please sign in instead."}), 409

    # Generate OTP and expiry (5 minutes)
    otp = generate_otp()
    expires_at = (datetime.now() + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")

    # Store OTP in database
    if not store_otp(email, otp, expires_at):
        return jsonify({"message": "Failed to generate OTP. Please try again."}), 500

    # Send OTP via email
    email_sent = send_otp_email(email, otp)
    if not email_sent:
        return jsonify({"message": "Failed to send OTP email. Please try again."}), 500

    return jsonify({
        "status": "success",
        "message": "Verification code sent to your email"
    }), 200


# ============================================================
# Verify OTP (for sign-up)
# ============================================================

@user_bp.route("/verify_signup_otp", methods=["POST"])
def verify_signup_otp():
    data = request.json
    email = data.get("email", "").strip()
    otp = data.get("otp", "").strip()

    if not email or not otp:
        return jsonify({"message": "Email and verification code are required"}), 400

    # Verify OTP
    if not verify_otp(email, otp):
        return jsonify({"message": "Invalid or expired verification code."}), 401

    return jsonify({
        "status": "success",
        "message": "Email verified successfully!"
    }), 200


# ============================================================
# Finalize Registration
# ============================================================

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    phone_number = data.get("phone_number", "").strip()
    if any(char.isupper() for char in email):
        return jsonify({"message": "Please enter email in lowercase letters only."}), 400
    password = data.get("password", "")

    if not all([name, email, phone_number, password]):
        return jsonify({"message": "Missing fields"}), 400

    # Validate password strength
    is_valid, error_msg = validate_password(password)
    if not is_valid:
        return jsonify({"message": error_msg}), 400

    # Create user account and set as verified
    user_id = create_user(name, email, phone_number, password, is_verified=True)
    if not user_id:
        return jsonify({"message": "Failed to create account"}), 500
    
    # Generate initial daily plan
    generate_daily_plan(user_id)

    # Clean up OTP
    delete_otp(email)

    return jsonify({
        "status": "success",
        "message": "Account created successfully!",
        "user_id": user_id
    }), 201


# ============================================================
# Login User
# ============================================================

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email", "").strip()
    if any(char.isupper() for char in email):
        return jsonify({"message": "Please enter email in lowercase letters only."}), 400
    password = data.get("password", "")

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    user = get_user_by_email(email)
    if user and user["password"] == password:
        if not user.get("is_verified", False):
            return jsonify({"message": "Please verify your email before signing in."}), 403
            
        user_info = {k: v for k, v in user.items() if k != 'password'}
        return jsonify({
            "status": "success",
            "message": "Login successful", 
            "user": user_info
        }), 200
    
    return jsonify({"message": "Invalid initials. Please check your email and password."}), 401


# ============================================================
# Forgot Password - Send Reset Code
# ============================================================

@user_bp.route("/forgot_password", methods=["POST"])
def forgot_password():
    data = request.json
    email = data.get("email", "").strip()
    if any(char.isupper() for char in email):
        return jsonify({"message": "Please enter email in lowercase letters only."}), 400

    if not email:
        return jsonify({"message": "Please enter a valid email address."}), 400

    # Check if user exists
    user = get_user_by_email(email)
    if not user:
        return jsonify({"message": "No account found with this email address."}), 404

    # Generate OTP with 5-minute expiry
    otp = generate_otp()
    expires_at = (datetime.now() + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")

    # Store in OTP table
    if not store_otp(email, otp, expires_at):
        return jsonify({"message": "Failed to generate reset code."}), 500

    # Send email
    email_sent = send_password_reset_email(email, otp)
    if not email_sent:
        return jsonify({"message": "Failed to send reset email."}), 500

    return jsonify({
        "status": "success",
        "message": "Reset code sent to your email"
    }), 200


# ============================================================
# Forgot Password - Verify Reset Code
# ============================================================

@user_bp.route("/verify_reset_otp", methods=["POST"])
def verify_reset_otp():
    data = request.json
    email = data.get("email", "").strip()
    otp = data.get("otp", "").strip()

    if not email or not otp:
        return jsonify({"message": "Email and reset code are required"}), 400

    if not verify_otp(email, otp):
        return jsonify({"message": "Invalid or expired reset code."}), 401

    return jsonify({
        "status": "success",
        "message": "Code verified successfully."
    }), 200


# ============================================================
# Forgot Password - Reset Password
# ============================================================

@user_bp.route("/reset_password", methods=["POST"])
def reset_password():
    data = request.json
    email = data.get("email", "").strip()
    otp = data.get("otp", "").strip()
    new_password = data.get("new_password", "")

    if not all([email, otp, new_password]):
        return jsonify({"message": "Missing required fields"}), 400

    # Validate the new password
    is_valid, error_msg = validate_password(new_password)
    if not is_valid:
        return jsonify({"message": error_msg}), 400

    # Verify the OTP is still valid
    if not verify_otp(email, otp):
        return jsonify({"message": "Invalid or expired reset code."}), 401

    # Reset the password
    success = reset_password_by_email(email, new_password)
    if not success:
        return jsonify({"message": "Failed to reset password."}), 500

    # Clean up the OTP
    delete_otp(email)

    return jsonify({
        "status": "success",
        "message": "Password reset successfully"
    }), 200


# ============================================================
# Update Profile & Generate Plan
# ============================================================

@user_bp.route("/update_profile", methods=["POST"])
def update_profile():
    data = request.json
    user_id = data.get("user_id")
    profile_data = data.get("profile")

    if user_id is None or not profile_data:
        return jsonify({"message": "Missing user_id or profile data"}), 400

    try:
        success = update_user_profile(user_id, profile_data)
        if success:
            # Regenerate daily plan whenever profile changes
            generate_daily_plan(user_id)
            return jsonify({"message": "Profile updated and plan generated successfully"}), 200
        else:
            return jsonify({"message": "Database connection failed"}), 500
    except Exception as e:
        print(f"Error in update_profile: {e}")
        return jsonify({"message": str(e)}), 500


# ============================================================
# Get Daily Plan
# ============================================================

@user_bp.route("/plan/<int:user_id>", methods=["GET"])
def get_plan(user_id):
    conn = get_db_connection()
    if not conn: return jsonify({"message": "DB connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM daily_plans WHERE user_id = %s", (user_id,))
    plans = cursor.fetchall()
    
    for plan in plans:
        pose_ids = plan['pose_ids'].split(',')
        if pose_ids:
            placeholders = ', '.join(['%s'] * len(pose_ids))
            cursor.execute(f"SELECT * FROM yoga_poses WHERE id IN ({placeholders})", tuple(pose_ids))
            plan['poses'] = cursor.fetchall()
        else:
            plan['poses'] = []
            
    conn.close()
    return jsonify(plans)


# ============================================================
# Change Password (for logged-in users)
# ============================================================

@user_bp.route("/change_password", methods=["POST"])
def change_password():
    data = request.json
    user_id = data.get("user_id")
    old_password = data.get("old_password")
    new_password = data.get("new_password")

    if not all([user_id, old_password, new_password]):
        return jsonify({"message": "Missing fields"}), 400

    # Validate new password strength
    is_valid, error_msg = validate_password(new_password)
    if not is_valid:
        return jsonify({"message": error_msg}), 400
        
    conn = get_db_connection()
    if not conn: return jsonify({"message": "DB error"}), 500
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT password FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if not user or user["password"] != old_password:
        return jsonify({"message": "Invalid old password"}), 401
        
    success = change_user_password(user_id, new_password)
    if success:
        return jsonify({"message": "Password updated successfully"}), 200
    return jsonify({"message": "Failed to update password"}), 500


# ============================================================
# Progress Tracking
# ============================================================

@user_bp.route("/add_progress", methods=["POST"])
def save_progress():
    data = request.json
    user_id = data.get("user_id")
    progress_data = data.get("progress")

    if user_id is None or not progress_data:
        return jsonify({"message": "Missing user_id or progress data"}), 400

    try:
        add_user_progress(user_id, progress_data)
        return jsonify({"message": "Progress saved successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@user_bp.route("/get_progress/<int:user_id>", methods=["GET"])
def get_progress(user_id):
    try:
        history = get_user_progress_history(user_id)
        return jsonify(history), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@user_bp.route("/get_stats/<int:user_id>", methods=["GET"])
def get_stats(user_id):
    try:
        stats = get_user_stats(user_id)
        if stats:
            return jsonify(stats), 200
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@user_bp.route("/get_activity/<int:user_id>", methods=["GET"])
def get_activity(user_id):
    try:
        activities = get_user_activity(user_id)
        return jsonify(activities), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# ============================================================
# Image Upload
# ============================================================

import os
import time
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/journey_shots'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@user_bp.route("/upload_image", methods=["POST"])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"message": "No image part"}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    
    if file:
        filename = secure_filename(f"{int(time.time())}_{file.filename}")
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        return jsonify({"image_path": filepath}), 201
    
    return jsonify({"message": "Upload failed"}), 500


# ============================================================
# Delete Account
# ============================================================

@user_bp.route("/delete_account", methods=["DELETE"])
def delete_account():
    user_id = request.json.get("user_id") if request.json else None

    if not user_id:
        return jsonify({"message": "user_id is required"}), 400

    conn = get_db_connection()
    if not conn:
        return jsonify({"message": "Database connection failed"}), 500

    try:
        cursor = conn.cursor()

        # Verify user exists first
        cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
        if not cursor.fetchone():
            conn.close()
            return jsonify({"message": "User not found"}), 404

        # Delete in proper FK order: child tables first, then parent
        cursor.execute("DELETE FROM sessions WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM user_progress WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM daily_plans WHERE user_id = %s", (user_id,))

        # Delete OTPs by user email
        cursor.execute("SELECT email FROM users WHERE id = %s", (user_id,))
        user_row = cursor.fetchone()
        if user_row:
            email = user_row[0]
            cursor.execute("DELETE FROM otps WHERE email = %s", (email,))

        # Finally delete the user
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        conn.close()

        return jsonify({
            "status": "success",
            "message": "Account permanently deleted."
        }), 200

    except Exception as e:
        conn.rollback()
        conn.close()
        print(f"Error deleting account: {e}")
        return jsonify({"message": f"Failed to delete account: {str(e)}"}), 500
