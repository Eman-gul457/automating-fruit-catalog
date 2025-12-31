# 🥭 Automating Updates to Fruit Catalog Information

## 📌 Project Overview

This project automates how an **online fruit store** updates its product catalog using data provided by suppliers.

Suppliers send:
- Fruit **images** in `.tiff` format
- Fruit **details** (name, weight, description) in `.txt` files

Manually updating a website using these files is slow and error-prone.  
This project **fully automates the process** — from downloading supplier data to updating the website, generating reports, sending emails, and monitoring system health.

This work was completed as part of a **Google IT Automation with Python** hands-on lab.

---

## 🎯 What Problem Does This Solve? 

Imagine a store that receives hundreds of product images and descriptions every month.

Instead of:
- resizing images manually
- uploading them one by one
- typing product details by hand
- creating reports manually
- checking if the system is healthy

This automation:
✔ does everything automatically  
✔ reduces human mistakes  
✔ saves time  
✔ alerts you if something breaks  

---

## 🧠 What This Project Demonstrates

- Real-world **Python automation**
- Image processing
- Backend API interaction
- PDF report generation
- Email automation
- System monitoring (DevOps basics)

---

## 🛠 Technologies Used

- **Python**
- **Pillow (PIL)** – image processing
- **Requests** – HTTP uploads & API calls
- **Django REST Framework** – backend API
- **ReportLab** – PDF generation
- **SMTP / Email libraries** – email automation
- **psutil, shutil, socket** – system health monitoring
- **Linux CLI** – permissions, cron jobs

---

## 📂 Project Files (Created by Me)

| File Name | Purpose |
|----------|--------|
| `changeImage.py` | Converts `.tiff` images to `.jpeg` and resizes them |
| `supplier_image_upload.py` | Uploads processed images to the web server |
| `run.py` | Uploads fruit data (name, weight, description) to Django API |
| `reports.py` | Generates a PDF report |
| `emails.py` | Creates and sends emails |
| `report_email.py` | Sends the PDF report via email |
| `health_check.py` | Monitors system health and sends alerts |

### 🧪 Lab-Provided Scripts (Not Written by Me)
- `download_bucket_file.sh`
- `example_upload.py`

These were provided by the lab and are mentioned for completeness.

---

## 🔄 Step-by-Step Workflow

### 1️⃣ Download Supplier Data
Supplier data is downloaded from a cloud bucket and extracted.

```bash
sudo chmod +x download_bucket_file.sh
./download_bucket_file.sh
tar xf supplier-data.tar.gz
```
---
This creates:
•supplier-data/images/
•supplier-data/descriptions/

----
### 2️⃣ Process Images (TIFF → JPEG)
Supplier images are:
•converted from .tiff → .jpeg
•resized to 600x400
•converted from RGBA → RGB
```bash
sudo chmod +x changeImage.py
./changeImage.py
```
<img width="1057" height="594" alt="python project screenshot 1" src="https://github.com/user-attachments/assets/13bb50a6-89b5-42bd-b6ca-43ae5b7dc152" />

---
### 3️⃣ Upload Images to Web Server
Images are uploaded to the Django server using HTTP requests.
```bash
sudo chmod +x supplier_image_upload.py
./supplier_image_upload.py
```
<img width="957" height="650" alt="python project screenshot 2" src="https://github.com/user-attachments/assets/3769a386-1ae4-4c5e-b9af-8dcdfbf50270" />

---
### 4️⃣ Upload Fruit Data to Django API
Fruit data is read from .txt files and uploaded as JSON.
```bash
sudo chmod +x run.py
./run.py
```
Each fruit includes:
•name
•weight (integer)
•description
•image name
<img width="633" height="398" alt="image" src="https://github.com/user-attachments/assets/e7467d24-7847-45f2-92b1-96d17a6e3f33" />

---

### 5️⃣ Generate PDF Report
A PDF report is generated showing:
•fruit names
•total weights
```bash
sudo chmod +x report_email.py
./report_email.py
```
•Email received
•PDF attached
•PDF opened successfully

<img width="513" height="421" alt="python project screenshot 9" src="https://github.com/user-attachments/assets/4436b242-4333-4b79-a49c-9caf13f93776" />

---
### 6️⃣ Email Notification

An automated email is sent to confirm successful upload.
•Email includes:
•Subject: Upload Completed - Online Fruit Store
•PDF attachment

<img width="1365" height="676" alt="python project screenshot 6" src="https://github.com/user-attachments/assets/9715331d-81d2-42ec-9ee1-167868054601" />

---
### 7️⃣ System Health Monitoring

The system is continuously monitored for:
•CPU usage > 80%
•Disk space < 20%
•Available memory < 100MB
•DNS resolution failure
```bash
sudo chmod +x health_check.py
./health_check.py
```
If an issue is detected, an alert email is sent automatically.

<img width="1337" height="641" alt="python project screenshot 8" src="https://github.com/user-attachments/assets/1989bc7b-bd2d-4331-ae7d-25e7ab5e1236" />

---

⏱ Cron Job (Automation)

The health check script is scheduled to run every 60 seconds using cron.
```bash
crontab -e
```
<img width="1365" height="637" alt="python project screenshot 7" src="https://github.com/user-attachments/assets/de1d7c6c-0694-4c9d-86cf-0540d79bdc44" />


This screenshot shows repeated alert emails arriving at regular intervals, confirming that the health check script is running automatically every minute via cron.

---
🏁 Final Result
---
✔ Automated catalog updates
✔ Live website updated
✔ PDF report generated
✔ Email notifications sent
✔ System health monitored

This project simulates real production automation used in e-commerce and DevOps environments.

----

📚 Credits
---
This project was completed as part of a Google IT Automation with Python lab.
All automation scripts were written and executed by me.
Screenshots are included as proof of work.

---
