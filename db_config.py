import mysql.connector
from mysql.connector import Error

# XAMPP Default Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '', # Default XAMPP MySQL password is empty
    'database': 'yoga_app_db'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def init_db():
    try:
        # Connect without database to create it if it doesn't exist
        temp_conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        cursor = temp_conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        temp_conn.close()

        # Connect to the target database
        conn = get_db_connection()
        if not conn:
            return
            
        cursor = conn.cursor()
        
        # Create Users table with all profile fields
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                is_verified BOOLEAN DEFAULT FALSE,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                age VARCHAR(50),
                gender VARCHAR(50),
                height VARCHAR(50),
                weight VARCHAR(50),
                goal VARCHAR(255),
                activityLevel VARCHAR(255),
                experience VARCHAR(255),
                focusArea VARCHAR(255),
                frequency VARCHAR(255)
            )
        ''')
        
        try:
            cursor.execute("ALTER TABLE users ADD COLUMN is_verified BOOLEAN DEFAULT FALSE AFTER password")
        except: pass

        try:
            cursor.execute("ALTER TABLE users ADD COLUMN phone_number VARCHAR(20) AFTER is_verified")
        except: pass

        try:
            cursor.execute("ALTER TABLE users ADD COLUMN bio TEXT AFTER phone_number")
        except: pass

        try:
            cursor.execute("ALTER TABLE users ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP AFTER bio")
        except: pass
        
        # Create Yoga Poses table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS yoga_poses (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description TEXT,
                difficulty VARCHAR(50)
            )
        ''')
        
        # Create Daily Plans table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS daily_plans (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                day_number INT,
                pose_ids TEXT, -- Comma separated pose IDs
                is_completed BOOLEAN DEFAULT FALSE,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Create Sessions table (for history)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                pose_id INT,
                duration INT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # Create Journey Shots table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS journey_shots (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                weight VARCHAR(50),
                height VARCHAR(50),
                age VARCHAR(50),
                health_status VARCHAR(255),
                image_path VARCHAR(255),
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # Create Session Summaries table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS session_summaries (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                style_name VARCHAR(255),
                level VARCHAR(50),
                total_duration INT,
                actual_duration INT,
                completion_percentage FLOAT,
                status VARCHAR(50),
                calories INT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Create OTP Verifications table (Match user's Step 4 requirement)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS otp_verifications (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                otp_code VARCHAR(6) NOT NULL,
                expires_at DATETIME NOT NULL
            )
        ''')

        # Ensure otp_code column exists if table already existed with 'otp'
        try:
            cursor.execute("ALTER TABLE otp_verifications CHANGE otp otp_code VARCHAR(6) NOT NULL")
        except: pass

        conn.commit()
        conn.close()
        print(f"MySQL database '{DB_CONFIG['database']}' initialized successfully.")
    except Error as e:
        print(f"Error initializing MySQL database: {e}")

if __name__ == "__main__":
    init_db()
