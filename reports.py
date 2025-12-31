#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report.build([
        Paragraph(title, styles["h1"]),
        Paragraph(paragraph, styles["Normal"])
    ])
