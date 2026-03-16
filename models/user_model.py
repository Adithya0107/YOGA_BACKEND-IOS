from db_config import get_db_connection
import json

def create_user(name, email, phone_number, password, is_verified=False):
    conn = get_db_connection()
    if not conn: return None
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, phone_number, password, is_verified) VALUES (%s, %s, %s, %s, %s)",
            (name, email, phone_number, password, is_verified)
        )
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        print(f"Error creating user: {e}")
        return None
    finally:
        conn.close()

def set_user_verified(email):
    """Mark a user as verified after successful OTP verification."""
    conn = get_db_connection()
    if not conn: return False
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET is_verified = TRUE WHERE email = %s", (email,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error setting user verified: {e}")
        return False
    finally:
        conn.close()

def update_user_profile(user_id, profile_data):
    try:
        conn = get_db_connection()
        if not conn: return False
        cursor = conn.cursor()
        
        query = """
            UPDATE users 
            SET name=%s, bio=%s, phone_number=%s,
                age=%s, gender=%s, height=%s, weight=%s, 
                goal=%s, activityLevel=%s, experience=%s, 
                focusArea=%s, frequency=%s 
            WHERE id=%s
        """
        params = (
            profile_data.get('name'),
            profile_data.get('bio'),
            profile_data.get('phone_number'),
            profile_data.get('age'),
            profile_data.get('gender'),
            profile_data.get('height'),
            profile_data.get('weight'),
            profile_data.get('goal'),
            profile_data.get('activityLevel'),
            profile_data.get('experience'),
            profile_data.get('focusArea'),
            profile_data.get('frequency'),
            user_id
        )
        
        cursor.execute(query, params)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating user profile: {e}")
        return False
    finally:
        if conn: conn.close()

def generate_daily_plan(user_id):
    conn = get_db_connection()
    if not conn: return
    try:
        cursor = conn.cursor(dictionary=True)
        # Get user experience to filter poses
        cursor.execute("SELECT experience FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        exp = user['experience'].lower() if user else 'beginner'
        
        if exp == 'all':
            cursor.execute("SELECT id FROM yoga_poses ORDER BY RAND() LIMIT 5")
        else:
            difficulty = 'beginner'
            if 'intermediate' in exp: difficulty = 'intermediate'
            if 'advanced' in exp: difficulty = 'advanced'
            cursor.execute("SELECT id FROM yoga_poses WHERE difficulty = %s ORDER BY RAND() LIMIT 5", (difficulty,))
        
        poses = cursor.fetchall()
        if len(poses) < 3:
            cursor.execute("SELECT id FROM yoga_poses ORDER BY RAND() LIMIT 5")
            poses = cursor.fetchall()
            
        pose_ids = ",".join([str(p['id']) for p in poses])
        for day in range(1, 8):
            cursor.execute(
                "INSERT INTO daily_plans (user_id, day_number, pose_ids) VALUES (%s, %s, %s)",
                (user_id, day, pose_ids)
            )
        conn.commit()
    except Exception as e:
        print(f"Error generating daily plan: {e}")
    finally:
        conn.close()

def get_user_by_email(email):
    conn = get_db_connection()
    if not conn: return None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error getting user by email: {e}")
        return None
    finally:
        conn.close()

def get_all_users():
    conn = get_db_connection()
    if not conn: return []
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
    except Exception as e:
        print(f"Error getting all users: {e}")
        return []
    finally:
        conn.close()

def change_user_password(user_id, new_password):
    conn = get_db_connection()
    if not conn: return False
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET password = %s WHERE id = %s", (new_password, user_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error changing password: {e}")
        return False
    finally:
        conn.close()

def add_user_progress(user_id, progress_data):
    conn = get_db_connection()
    if not conn: return
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO journey_shots (user_id, weight, height, age, health_status, image_path)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (
            user_id,
            progress_data.get('weight'),
            progress_data.get('height'),
            progress_data.get('age'),
            progress_data.get('health_status'),
            progress_data.get('image_path')
        )
        cursor.execute(query, params)
        conn.commit()
    except Exception as e:
        print(f"Error adding progress: {e}")
    finally:
        conn.close()

def get_user_progress_history(user_id):
    conn = get_db_connection()
    if not conn: return []
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM journey_shots WHERE user_id = %s ORDER BY timestamp DESC", (user_id,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error getting progress history: {e}")
        return []
    finally:
        conn.close()

def get_user_stats(user_id):
    conn = get_db_connection()
    if not conn: return None
    try:
        cursor = conn.cursor(dictionary=True)
        
        # 1. Get total minutes and session count from session_summaries
        cursor.execute("""
            SELECT SUM(actual_duration) as total_seconds, COUNT(*) as sessions 
            FROM session_summaries WHERE user_id = %s
        """, (user_id,))
        res = cursor.fetchone()
        total_minutes = int(res['total_seconds'] or 0) // 60
        sessions = res['sessions'] or 0
        
        # 2. Get current streak (unique days in the last 30 days)
        cursor.execute("""
            SELECT COUNT(DISTINCT DATE(timestamp)) as streak_days 
            FROM session_summaries 
            WHERE user_id = %s AND timestamp >= DATE_SUB(NOW(), INTERVAL 30 DAY)
        """, (user_id,))
        streak_res = cursor.fetchone()
        streak_days = streak_res['streak_days'] or 0
        
        # 3. Get BMI/Health from latest journey_shot
        cursor.execute("""
            SELECT weight, height, health_status FROM journey_shots 
            WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1
        """, (user_id,))
        shot = cursor.fetchone()
        
        bmi = 0.0
        health_status = "Normal"
        if shot:
            try:
                w = float(shot['weight'])
                h = float(shot['height']) / 100.0 # to meters
                if h > 0:
                    bmi = w / (h * h)
                health_status = shot['health_status'] or "Normal"
            except: pass
        
        return {
            "level": 1, 
            "streak_days": streak_days,
            "total_minutes": total_minutes,
            "sessions": sessions,
            "bmi": round(bmi, 1),
            "health_status": health_status,
            "recovery_rate": 80 
        }
    except Exception as e:
        print(f"Error getting user stats: {e}")
        return None
    finally:
        conn.close()

def get_user_activity(user_id):
    conn = get_db_connection()
    if not conn: return []
    try:
        cursor = conn.cursor(dictionary=True)
        # Return last 30 days of activity
        cursor.execute("""
            SELECT DATE_FORMAT(timestamp, '%Y-%m-%d') as date, 
                   SUM(actual_duration) DIV 60 as minutes,
                   'done' as status
            FROM session_summaries 
            WHERE user_id = %s 
            GROUP BY DATE(timestamp)
            ORDER BY timestamp DESC
            LIMIT 30
        """, (user_id,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error getting user activity: {e}")
        return []
    finally:
        conn.close()


# ============================================================
# OTP Verification (Signup & Reset)
# ============================================================

def store_otp(email, otp_code, expires_at):
    """Store or update OTP for either sign-up or password reset."""
    conn = get_db_connection()
    if not conn: return False
    try:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO otp_verifications (email, otp_code, expires_at) 
               VALUES (%s, %s, %s) 
               ON DUPLICATE KEY UPDATE otp_code = VALUES(otp_code), expires_at = VALUES(expires_at)""",
            (email, otp_code, expires_at)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error storing OTP: {e}")
        return False
    finally:
        conn.close()

def verify_otp(email, otp_code):
    """Verify OTP code. Returns True if valid and not expired."""
    conn = get_db_connection()
    if not conn: return False
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT otp_code, expires_at FROM otp_verifications WHERE email = %s AND otp_code = %s AND expires_at > NOW()",
            (email, otp_code)
        )
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"Error verifying OTP: {e}")
        return False
    finally:
        conn.close()

def delete_otp(email):
    """Remove OTP record after successful verification."""
    conn = get_db_connection()
    if not conn: return
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM otp_verifications WHERE email = %s", (email,))
        conn.commit()
    except Exception as e:
        print(f"Error deleting OTP: {e}")
    finally:
        conn.close()

def reset_password_by_email(email, new_password):
    """Reset a user's password using their email address."""
    conn = get_db_connection()
    if not conn: return False
    try:
        cursor = conn.cursor()
        # When resetting password, we also ensure the user is marked as verified
        cursor.execute("UPDATE users SET password = %s, is_verified = TRUE WHERE email = %s", (new_password, email))
        affected = cursor.rowcount
        conn.commit()
        return affected > 0
    except Exception as e:
        print(f"Error resetting password: {e}")
        return False
    finally:
        conn.close()

