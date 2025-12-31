#!/usr/bin/env python3

import shutil
import psutil
import socket
import time
import emails

def check():
    if psutil.cpu_percent() > 80:
        return "Error - CPU usage is over 80%"
    if shutil.disk_usage("/").free / shutil.disk_usage("/").total < 0.2:
        return "Error - Available disk space is less than 20%"
    if psutil.virtual_memory().available < 100 * 1024 * 1024:
        return "Error - Available memory is less than 100MB"
    if socket.gethostbyname("localhost") != "127.0.0.1":
        return "Error - localhost cannot be resolved to 127.0.0.1"
    return None

while True:
    error = check()
    if error:
        message = emails.generate_email(
            "automation@example.com",
            "student@example.com",
            error,
            "Please check your system and resolve the issue as soon as possible."
        )
        emails.send_email(message)
    time.sleep(60)
