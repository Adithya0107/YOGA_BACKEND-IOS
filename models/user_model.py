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
            SET name=COALESCE(%s, name), bio=COALESCE(%s, bio), phone_number=COALESCE(%s, phone_number),
                age=COALESCE(%s, age), gender=COALESCE(%s, gender), height=COALESCE(%s, height), weight=COALESCE(%s, weight), 
                goal=COALESCE(%s, goal), activityLevel=COALESCE(%s, activityLevel), experience=COALESCE(%s, experience), 
                focusArea=COALESCE(%s, focusArea), frequency=COALESCE(%s, frequency), dietaryPreference=COALESCE(%s, dietaryPreference) 
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
            profile_data.get('dietaryPreference'),
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
        # Clear existing daily plans first to make it dynamic
        cursor.execute("DELETE FROM daily_plans WHERE user_id = %s", (user_id,))
        
        # Get user experience to filter poses
        cursor.execute("SELECT experience FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        exp = user['experience'].lower() if (user and user['experience']) else 'beginner'
        
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
        # Generate for 7 days
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
    if not conn: return False
    try:
        cursor = conn.cursor(dictionary=True)
        
        # 1. Get current streak
        stats = get_user_stats(user_id)
        if not stats: return False
        streak = int(stats.get('streak_days', 0))
        
        # 2. Get current shot count
        cursor.execute("SELECT COUNT(*) as count FROM journey_shots WHERE user_id = %s", (user_id,))
        count_res = cursor.fetchone()
        shot_count = int(count_res['count'] if count_res else 0)
        
        # Requirement: For every 15 days of streak, 1 shot is allowed
        # Max allowed shots = streak // 15
        if streak < 15:
            # First shot requires at least 15 days
            return False
        
        if shot_count >= (streak // 15):
            # Already uploaded shots for all available milestones
            return False
            
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
        return True
    except Exception as e:
        print(f"Error adding progress: {e}")
        return False
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
        
        # 2. Get current streak (consecutive days with 2-day grace)
        cursor.execute("""
            SELECT DISTINCT DATE(timestamp) as practice_date 
            FROM session_summaries 
            WHERE user_id = %s 
            ORDER BY practice_date DESC
        """, (user_id,))
        dates = cursor.fetchall()
        
        streak_days = 0
        if dates:
            from datetime import date
            today = date.today()
            last_practice = dates[0]['practice_date']
            
            # If gap between today and last practice >= 3 days, streak resets (reduced)
            if (today - last_practice).days >= 3:
                streak_days = 0
            else:
                # Count consecutive practice days where each gap is < 3 days
                streak_days = 1
                for i in range(1, len(dates)):
                    gap = (dates[i-1]['practice_date'] - dates[i]['practice_date']).days
                    if gap < 3:
                        streak_days += 1
                    else:
                        break
        
        # Calculate level based on sessions (Dynamic leveling)
        level = (sessions // 5) + 1
        if level > 50: level = 50 # Cap level at 50
        
        # 3. Get BMI/Health from User Profile (Source of Truth)
        cursor.execute("""
            SELECT weight, height, age, goal FROM users WHERE id = %s
        """, (user_id,))
        user_prof = cursor.fetchone()
        
        bmi = 0.0
        health_status = "Normal"
        current_weight = 0
        current_height = 0
        current_age = 0

        if user_prof:
            try:
                current_weight = float(user_prof['weight'] or 0)
                current_height = float(user_prof['height'] or 0)
                current_age = int(user_prof['age'] or 0)
                
                h_meters = current_height / 100.0
                if h_meters > 0:
                    bmi = current_weight / (h_meters * h_meters)
            except: pass

        # Get latest health_status from journey_shots as secondary
        cursor.execute("""
            SELECT health_status FROM journey_shots 
            WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1
        """, (user_id,))
        shot = cursor.fetchone()
        if shot and shot['health_status']:
            health_status = shot['health_status']
        else:
            # Fallback status based on BMI
            if bmi > 0:
                health_status = "Underweight" if bmi < 18.5 else "Normal" if bmi < 25 else "Overweight" if bmi < 30 else "Obese"
        
        return {
            "level": level, 
            "streak_days": int(streak_days),
            "total_minutes": int(total_minutes),
            "sessions": int(sessions),
            "bmi": round(bmi, 1),
            "health_status": health_status,
            "recovery_rate": 80,
            "weight": current_weight,
            "height": current_height,
            "age": current_age
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
        # Return last 90 days of activity for calendar and graph
        cursor.execute("""
            SELECT DATE_FORMAT(timestamp, '%%Y-%%m-%%d') as date, 
                   COALESCE(SUM(actual_duration) DIV 60, 0) as minutes,
                   'done' as status
            FROM session_summaries 
            WHERE user_id = %s 
              AND timestamp >= DATE_SUB(CURDATE(), INTERVAL 90 DAY)
            GROUP BY DATE(timestamp)
            ORDER BY date DESC
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

