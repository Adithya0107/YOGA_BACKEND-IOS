from db_config import get_db_connection

def create_pose(name, description, difficulty):
    conn = get_db_connection()
    if not conn: return
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO yoga_poses (name, description, difficulty) VALUES (%s, %s, %s)",
        (name, description, difficulty)
    )
    conn.commit()
    conn.close()

def get_all_poses():
    conn = get_db_connection()
    if not conn: return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM yoga_poses")
    poses = cursor.fetchall()
    conn.close()
    return poses

def save_session_summary(user_id, style_name, level, total_duration, actual_duration, completion_percentage, status, calories):
    conn = get_db_connection()
    if not conn: return False
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO session_summaries (user_id, style_name, level, total_duration, actual_duration, completion_percentage, status, calories) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (user_id, style_name, level, total_duration, actual_duration, completion_percentage, status, calories)
    )
    conn.commit()
    conn.close()
    return True
