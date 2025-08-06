import requests
import hashlib
import os
import smtplib
from email.message import EmailMessage

# ------------------------------
# ✏️ CONFIGURATION - UPDATE THIS
# ------------------------------

URL = 'https://www.geo.tv/'  # Replace with the site you want to monitor
YOUR_EMAIL = 'moonknight0921@gmail.com'
APP_PASSWORD = 'rfwdynxkbcmprqfo'  # 16-character Gmail app password

DATA_FILE = 'last_hash.txt'

# ------------------------------

def get_page_hash(url):
    response = requests.get(url)
    return hashlib.md5(response.text.encode('utf-8')).hexdigest()

def load_last_hash():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return f.read().strip()
    return ''

def save_hash(hash_value):
    with open(DATA_FILE, 'w') as f:
        f.write(hash_value)

def send_email():
    msg = EmailMessage()
    msg.set_content(f'🔔 The website at {URL} has changed!')

    msg['Subject'] = 'Website Update Detected!'
    msg['From'] = YOUR_EMAIL
    msg['To'] = YOUR_EMAIL

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(YOUR_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
        print("📧 Email sent!")

def main():
    current_hash = get_page_hash(URL)
    last_hash = load_last_hash()

    if current_hash != last_hash:
        print("🔔 Website content has changed!")
        send_email()
        save_hash(current_hash)
    else:
        print("✅ No change detected.")

if __name__ == "__main__":
    main()
