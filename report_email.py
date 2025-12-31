#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def main():
    path = os.path.expanduser('~/supplier-data/descriptions')
    paragraph = ""

    for file in os.listdir(path):
        with open(os.path.join(path, file)) as f:
            lines = f.read().split('\n')
            paragraph += f"name: {lines[0]}<br/>weight: {lines[1]}<br/><br/>"

    title = f"Processed Update on {datetime.date.today()}"
    attachment = "/tmp/processed.pdf"

    reports.generate_report(attachment, title, paragraph)

    message = emails.generate_email(
        "automation@example.com",
        "student@example.com",
        "Upload Completed - Online Fruit Store",
        "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        attachment
    )

    emails.send_email(message)

if __name__ == "__main__":
    main()
