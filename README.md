# Send Multiple Emails Python Project

This Python project demonstrates how to send multiple emails using Gmail as the SMTP server. It can be used for various purposes, such as sending notifications, newsletters, or announcements to multiple recipients.


## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Introduction

This Python project is designed to empower users with the capability to send multiple emails effortlessly, utilizing Gmail as the SMTP (Simple Mail Transfer Protocol) server. The project is not only a practical solution for sending bulk emails but also an educational resource for individuals looking to delve into Python programming and email automation.

## Prerequisites

Before running this project, you'll need the following:

- Python 3.x installed on your system.
- A Gmail account to use as the sender.
- Gmail App Password or regular password for authentication.
- Configuration details stored in a `.env` file (see below).

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/coderbiozed/send-multiple-email.git

2. Navigate to the project directory: 
   ```bash
   `cd send-multiple-email`

3. Install the required Python packages using pip:
   ```bash
   `pip install -r requirements.txt`

## Configuration

   ### Create a .env file in the project directory.
   ### Add the following configuration details to the .env file:

- SMTP_SERVER=smtp.gmail.com
- SMTP_PORT=587
- SENDER_EMAIL=your_email@gmail.com
- SMTP_PASSWORD=your_app_password


## Usage

   ### Run the Python script to send emails to the recipients:

   `python send_emails.py`

## Troubleshooting

If you encounter any issues, 
- 👉Make sure that your Gmail account settings allow less secure apps or use an App Password.
- 👉Double-check your .env file for correct configuration details.
- 👉Ensure that you have Python 3.x installed and the required packages installed from requirements.txt.

## License
This project is licensed under the MIT License - see the LICENSE file for details.