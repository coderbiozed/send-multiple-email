# Email Sender with Python

This Python script allows you to send test email messages to multiple recipients using the `smtplib` library. If you receive these test emails in your Gmail inbox, it means the program is working correctly.

## Prerequisites

Before running the program, make sure you have the following:

- Python installed on your system.
- Gmail account credentials (your Gmail email address and password).
- Access to a local SMTP server or the SMTP server's hostname and port if using a local server.
- A list of recipient email addresses.

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/coderbiozed/email-sender-python.git


# Navigate to the project directory:

> cd email-sender-python

 Run the Python script:

> python send_emails.py 

Configuration 

In the send_emails.py script, you can configure the following:

gmail_user: Your Gmail email address.
gmail_password: Your Gmail password.
smtp_server: Your local SMTP server's hostname or IP address.
smtp_port: Your local SMTP server's port number.
recipient_list: A list of recipient email addresses.