import requests
import hashlib
import os

URL = 'https://www.geo.tv/'  # Change to your target website
DATA_FILE = 'last_hash.txt'

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

def main():
    current_hash = get_page_hash(URL)
    last_hash = load_last_hash()

    if current_hash != last_hash:
        print("🔔 Website content has changed!")
        save_hash(current_hash)
    else:
        print("✅ No change detected.")

if __name__ == "__main__":
    main()
