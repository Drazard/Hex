# -*- coding: utf-8 -*-
import random
import requests
import sys
import time
print("========================================")
SSID = input("Enter Session ID: ")
#SSID = input("Enter Login Data: ")
print("========================================")

while True:
    time.sleep(1)
    ip = ".".join(map(str, (random.randint(1, 255) 
                        for _ in range(4))))
    cookies = dict(PHPSESSID=str(SSID))
    req = requests.get('https://legacy.hackerexperience.com/internet?ip=' + ip, cookies=cookies)
    result = req.text
    if "404 - Page not found" not in result:
        f = open("foundips.txt","a") #opens file with name of "ip.txt"
        f.write(ip+"\n")
        print ("SERVER FOUND! - "+ip)
    else:
        print(ip+" - not Found...")
        
