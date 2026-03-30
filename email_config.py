"""
Email configuration for sending OTPs via Gmail SMTP.

IMPORTANT: You need to set up a Gmail App Password for this to work.
Steps:
1. Go to https://myaccount.google.com/security
2. Enable 2-Step Verification
3. Go to App passwords (https://myaccount.google.com/apppasswords)
4. Generate a new app password for "Mail" on "Other (Custom name)"
5. Copy the 16-character password and paste it below as SMTP_PASSWORD

Replace the values below with your actual Gmail credentials.
"""

import smtplib
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# ============================================================
# ⚠️  UPDATE THESE WITH YOUR ACTUAL GMAIL CREDENTIALS  ⚠️
# ============================================================
SMTP_HOST = "smtp.gmail.com"
SMTP_EMAIL = "zenforgeyogafitnesstracker@gmail.com"
SMTP_PASSWORD = "fihk ykwi ucib zios"
SENDER_NAME = "ZenForge Yoga"
# ============================================================

# When True, if SMTP fails the OTP is printed to console
# and the function still returns True so the app flow isn't blocked.
DEV_FALLBACK = False


def _log_otp(to_email: str, otp: str, reason: str):
    """Log OTP prominently to console and debug file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. VISUAL TERMINAL BOX (Hard to miss)
    print("\n" + "!" * 60)
    print("🚀 [DEVELOPER OTP ALERT] 🚀")
    print(f"   EMAIL TO: {to_email}")
    print(f"   CODE IS : {otp}")
    print(f"   STATUS  : SMTP Blocked ({reason})")
    print("!" * 60 + "\n")

    # 2. SEPARATE DEBUG FILE (Easy to tail -f)
    try:
        import os
        log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "last_otp.txt")
        with open(log_path, "w") as f:
            f.write(f"OTP: {otp}\nEmail: {to_email}\nTime: {timestamp}")
    except:
        pass


def _try_send_email(msg, to_email: str) -> bool:
    """
    Try sending email using multiple SMTP strategies.
    Strategy 1: Port 465 with SMTP_SSL (most reliable)
    Strategy 2: Port 587 with STARTTLS
    Returns True on success, False on failure.
    """
    # Strategy 1: SMTP_SSL on port 465 (usually works even when 587 is blocked)
    try:
        with smtplib.SMTP_SSL(SMTP_HOST, 465, timeout=8) as server:
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.sendmail(SMTP_EMAIL, to_email, msg.as_string())
        print(f"✅ Email sent via SMTP_SSL (port 465) to {to_email}")
        return True
    except smtplib.SMTPAuthenticationError:
        print(f"❌ SMTP AUTH ERROR (port 465): App password is invalid or expired.")
        print(f"   → Go to https://myaccount.google.com/apppasswords to generate a new one.")
        return False
    except Exception as e:
        print(f"⚠️  SMTP_SSL (port 465) failed: {e}. Trying port 587...")

    # Strategy 2: STARTTLS on port 587
    try:
        with smtplib.SMTP(SMTP_HOST, 587, timeout=8) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.sendmail(SMTP_EMAIL, to_email, msg.as_string())
        print(f"✅ Email sent via STARTTLS (port 587) to {to_email}")
        return True
    except smtplib.SMTPAuthenticationError:
        print(f"❌ SMTP AUTH ERROR (port 587): App password is invalid or expired.")
        print(f"   → Go to https://myaccount.google.com/apppasswords to generate a new one.")
        return False
    except Exception as e:
        print(f"❌ STARTTLS (port 587) also failed: {e}")
        return False


def _build_otp_html(otp: str) -> str:
    return f"""\
<html>
<body style="margin:0; padding:0; background-color:#f4f0ff; font-family: 'Helvetica Neue', Arial, sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f0ff; padding: 40px 0;">
    <tr>
      <td align="center">
        <table width="420" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:20px; box-shadow: 0 10px 40px rgba(130,90,255,0.1); overflow:hidden;">
          <!-- Header -->
          <tr>
            <td style="background: linear-gradient(135deg, #6C3CE0, #41B6FF); padding: 35px 30px; text-align:center;">
              <h1 style="color:#ffffff; margin:0; font-size:26px; font-weight:800; letter-spacing:0.5px;">🧘 ZenForge</h1>
              <p style="color:rgba(255,255,255,0.85); margin:8px 0 0; font-size:14px;">Your Yoga & Wellness Journey</p>
            </td>
          </tr>
          <!-- Body -->
          <tr>
            <td style="padding: 40px 30px; text-align:center;">
              <h2 style="color:#1a1a2e; margin:0 0 10px; font-size:22px;">Verification Code</h2>
              <p style="color:#64748b; font-size:15px; margin:0 0 30px; line-height:1.5;">
                Use the code below to complete your verification. It expires in <strong>5 minutes</strong>.
              </p>
              <!-- OTP Code -->
              <div style="background: linear-gradient(135deg, #f6f2ff, #eef6ff); border: 2px solid #e0d4ff; border-radius:14px; padding:20px 30px; display:inline-block;">
                <span style="font-size:36px; font-weight:900; letter-spacing:12px; color:#6C3CE0;">{otp}</span>
              </div>
              <p style="color:#94a3b8; font-size:13px; margin:25px 0 0; line-height:1.5;">
                If you didn't request this code, you can safely ignore this email.
              </p>
            </td>
          </tr>
          <!-- Footer -->
          <tr>
            <td style="background-color:#faf8ff; padding:20px 30px; text-align:center; border-top:1px solid #f0ecff;">
              <p style="color:#a0a0b0; font-size:12px; margin:0;">© 2026 ZenForge. All rights reserved.</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""


def _build_reset_html(otp: str) -> str:
    return f"""\
<html>
<body style="margin:0; padding:0; background-color:#f4f0ff; font-family: 'Helvetica Neue', Arial, sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f0ff; padding: 40px 0;">
    <tr>
      <td align="center">
        <table width="420" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:20px; box-shadow: 0 10px 40px rgba(130,90,255,0.1); overflow:hidden;">
          <tr>
            <td style="background: linear-gradient(135deg, #E03C3C, #FF6B41); padding: 35px 30px; text-align:center;">
              <h1 style="color:#ffffff; margin:0; font-size:26px; font-weight:800;">🔐 Password Reset</h1>
              <p style="color:rgba(255,255,255,0.85); margin:8px 0 0; font-size:14px;">ZenForge Account Security</p>
            </td>
          </tr>
          <tr>
            <td style="padding: 40px 30px; text-align:center;">
              <h2 style="color:#1a1a2e; margin:0 0 10px; font-size:22px;">Reset Your Password</h2>
              <p style="color:#64748b; font-size:15px; margin:0 0 30px; line-height:1.5;">
                Use the code below to reset your password. It expires in <strong>10 minutes</strong>.
              </p>
              <div style="background: linear-gradient(135deg, #fff2f2, #fff6ee); border: 2px solid #ffd4d4; border-radius:14px; padding:20px 30px; display:inline-block;">
                <span style="font-size:36px; font-weight:900; letter-spacing:12px; color:#E03C3C;">{otp}</span>
              </div>
              <p style="color:#94a3b8; font-size:13px; margin:25px 0 0; line-height:1.5;">
                If you didn't request a password reset, you can safely ignore this email.
              </p>
            </td>
          </tr>
          <tr>
            <td style="background-color:#faf8ff; padding:20px 30px; text-align:center; border-top:1px solid #f0ecff;">
              <p style="color:#a0a0b0; font-size:12px; margin:0;">© 2026 ZenForge. All rights reserved.</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""


def send_otp_email(to_email: str, otp: str) -> bool:
    """
    Send a 6-digit OTP to the given email address using Gmail SMTP.
    Returns True on success, False on failure.
    If DEV_FALLBACK is True and SMTP fails, logs OTP and returns True anyway.
    """
    # DEVELOPMENT MODE BYPASS: If credentials are not set, just print to console
    if SMTP_EMAIL == "your-email@gmail.com" or SMTP_PASSWORD == "xxxx xxxx xxxx xxxx":
        print(f"\n[DEV MODE] Skipping email send. Your OTP for {to_email} is: {otp}\n")
        return True

    try:
        msg = MIMEMultipart("alternative")
        msg["From"] = f"{SENDER_NAME} <{SMTP_EMAIL}>"
        msg["To"] = to_email
        msg["Subject"] = "Your ZenForge Verification Code"

        text = f"""\
Hi there,

Your verification code for ZenForge is: {otp}

This code will expire in 5 minutes.

If you didn't request this code, please ignore this email.

– The ZenForge Team
"""
        msg.attach(MIMEText(text, "plain"))
        msg.attach(MIMEText(_build_otp_html(otp), "html"))

        sent = _try_send_email(msg, to_email)
        if sent:
            return True

        # SMTP failed — use dev fallback
        if DEV_FALLBACK:
            _log_otp(to_email, otp, "SMTP authentication or connection failed")
            return True  # Return True so the app flow continues

        return False

    except Exception as e:
        print(f"❌ Failed to send OTP email to {to_email}: {e}")
        if DEV_FALLBACK:
            _log_otp(to_email, otp, str(e))
            return True
        return False


def send_password_reset_email(to_email: str, otp: str) -> bool:
    """
    Send a password reset OTP to the given email address using Gmail SMTP.
    Returns True on success, False on failure.
    If DEV_FALLBACK is True and SMTP fails, logs OTP and returns True anyway.
    """
    # DEVELOPMENT MODE BYPASS
    if SMTP_EMAIL == "your-email@gmail.com" or SMTP_PASSWORD == "xxxx xxxx xxxx xxxx":
        print(f"\n[DEV MODE] Skipping password reset email. Your code for {to_email} is: {otp}\n")
        return True

    try:
        msg = MIMEMultipart("alternative")
        msg["From"] = f"{SENDER_NAME} <{SMTP_EMAIL}>"
        msg["To"] = to_email
        msg["Subject"] = "ZenForge Password Reset Code"

        text = f"""\
Hi there,

You requested a password reset for your ZenForge account.

Your password reset code is: {otp}

This code will expire in 10 minutes.

If you didn't request this, please ignore this email.

– The ZenForge Team
"""
        msg.attach(MIMEText(text, "plain"))
        msg.attach(MIMEText(_build_reset_html(otp), "html"))

        sent = _try_send_email(msg, to_email)
        if sent:
            return True

        # SMTP failed — use dev fallback
        if DEV_FALLBACK:
            _log_otp(to_email, otp, "SMTP authentication or connection failed (password reset)")
            return True

        return False

    except Exception as e:
        print(f"❌ Failed to send password reset email to {to_email}: {e}")
        if DEV_FALLBACK:
            _log_otp(to_email, otp, str(e))
            return True
        return False
