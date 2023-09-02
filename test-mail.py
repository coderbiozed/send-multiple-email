import smtplib
from decouple import config

# SMTP server configuration
smtp_server = config('SMTP_SERVER')
smtp_port = int(config('SMTP_PORT'))  # Convert the port to an integer

# SMTP authentication
smtp_user = 'your_email@gmail.com'  # Replace with your Gmail email address
smtp_password = 'your_app_password'  # Replace with your Gmail App Password

# Sender's email address
sender_email = config('SENDER_EMAIL')

# Read recipient email addresses from the file
with open('recipient_emails.txt', 'r') as file:
    recipient_list = [line.strip() for line in file]

# Set up the SMTP connection
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Start TLS encryption
    server.login(smtp_user, smtp_password)  # Log in to your Gmail account

    # Loop through the recipients and send emails
    for recipient_email in recipient_list:
        subject = "Test Message from Python, If you read this SMS in your Gmail inbox, my program is working fine"
        body = f"Hello, this is a test email sent to {recipient_email} from Python."
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(sender_email, recipient_email, message)
        print(f"Email sent to {recipient_email}")

print("All emails sent successfully.")
