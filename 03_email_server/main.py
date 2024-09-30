import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server settings (e.g., Gmail, Outlook, or your own server)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Email login credentials
SENDER_EMAIL = 'your-email@gmail.com'
SENDER_PASSWORD = 'your-email-password'

def send_email(receiver_email, subject, body):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, receiver_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    receiver_email = 'ivanpachecoleo23@gmail.com'
    subject = 'Test Email'
    body = 'This is a test email sent from Python!'
    send_email(receiver_email, subject, body)
