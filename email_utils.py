import smtplib
import os
from email.message import EmailMessage
from config import logger, SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD #TESTING
# from config import logger, SMTP_HOST, SMTP_PORT, SMTP_FROM


def send_status_email(to_address, subject, body, attachment_path=None):
    msg = EmailMessage()
    msg["From"] = SMTP_USER #TESTING
    # msg["From"] = SMTP_FROM
    msg["To"] = to_address
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
        msg.add_attachment(
            file_data, 
            maintype="text", 
            subtype="plain", 
            filename = file_name
        )
    
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls() #TESTING
            server.login(SMTP_USER, SMTP_PASSWORD) #TESTING
            server.send_message(msg)
        logger.info(f"Status email sent to: {to_address}")
    except Exception as e:
        logger.error(f"Failed to send status email: {e}")