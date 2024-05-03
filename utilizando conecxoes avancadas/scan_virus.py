import requests
import json
import hashlib
import configparser
import time
import os

def get_api_key(key_name):
    config = configparser.ConfigParser()
    config.read("secrets.ini")
    api_key = config["APIKeys"][key_name]
    return api_key

def check_virustotal_hash(token,hash):
    url = api_base + "/file/report"
    params = {
        "apikey": token,
        "resource": hash
    }
    response = requests.get(url, params=params)
    items = response.json()
    return items

def upload_virustotal_file(token, file_path):
    file_name = os.path.basename(file_path)
    url = api_base + "/file/scan"

    params = { 'apikey': token }

    files = { 'file': (file_name, open(file_path, 'rb')) }

    response = requests.post(
        url, 
        files=files,
        params=params
        )
    items = response.json()
    return items

def get_virustotal_comments(hash):
    return True

def hash_file(file_path):
    buff_size = 65535
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    sha1 = hashlib.sha1()
    with open(file_path,"rb") as f:
        while True:
            data = f.read(buff_size)
            if not data: break
            md5.update(data)
            sha256.update(data)
            sha1.update(data)

    return sha256.hexdigest()

token = get_api_key("VirusTotal")
api_base = "https://www.virustotal.com/vtapi/v2/"

target_file = input("Say the name of the file: ")

file_hash = hash_file(target_file)

file_check = check_virustotal_hash(token,file_hash)

if file_check["response_code"] == 1:
    print("Scan found")
    print(f"{file_check} cans testeds, {1} positive")
    print(f"more details can be found at {file_check}")
else:
    print("file not previously scanned")
    upload_virustotal_file(token,target_file)
    print("file uploaded successfully")
    for i in range(3):
        time.sleep(21)
        file_check = check_virustotal_hash(token,file_hash)
        if file_check["response_code"] == 1:
            print(f"{file_check} cans testeds, {1} positive")
            print(f"more details can be found at {file_check}")
            break

if file_check["response_code"] == 1:
    print("scans not finished try again")