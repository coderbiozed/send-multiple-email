import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from decouple import config

# Read SMTP configuration from .env file
smtp_server = config('SMTP_SERVER')
smtp_port = config('SMTP_PORT', default=25, cast=int)
smtp_username = config('SMTP_USERNAME')
smtp_password = config('SMTP_PASSWORD')

# Read sender details from the JSON configuration file
with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
    sender_email = config_data.get('sender_email', '')

# Read recipient email addresses from the 'recipient_emails.txt' file
with open('recipient_emails.txt', 'r') as recipient_file:
    recipient_emails = [line.strip() for line in recipient_file]

# Read message details from the 'message.txt' file
with open('message.txt', 'r') as message_file:
    message_lines = message_file.readlines()
    subject = message_lines[0].strip()
    body = ''.join(message_lines[1:]).strip()

# Create an SMTP connection to Mailtrap
server = SMTP(smtp_server, smtp_port)

# Authenticate with Mailtrap's SMTP service
server.login(smtp_username, smtp_password)

# Create the email content
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = ', '.join(recipient_emails)
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Send the email
server.sendmail(sender_email, recipient_emails, message.as_string())

# Close the SMTP server connection
server.quit()

print('Emails sent successfully.')
