import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipient_email, subject, body):
    # Setup the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the local SMTP server
    with smtplib.SMTP('localhost') as server:
        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent successfully!")

# Usage
send_email('shresthaankit444@gmail.com', 'shresthaankit222@gmail.com', 'Test Email', 'Hello, this is a test email!')
