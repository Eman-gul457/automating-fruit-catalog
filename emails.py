#!/usr/bin/env python3

import email.message
import mimetypes
import smtplib

def generate_email(sender, recipient, subject, body, attachment=None):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment:
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_type.split('/')
        with open(attachment, 'rb') as f:
            message.add_attachment(
                f.read(),
                maintype=mime_type,
                subtype=mime_subtype,
                filename=attachment
            )
    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
