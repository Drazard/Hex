import subprocess
import webbrowser
import sys
import requests
import time

SSID = input("Enter SSID: ")
cookies = dict(PHPSESSID=str(SSID))

    
f = open("ips.txt")
for line in f:
    url = "https://legacy.hackerexperience.com/internet?action=hack&method=bf&ip=" + line
    req = requests.get(url, cookies=cookies)
    result = req.text
    if "your cracker is not good enough." in result:
        print("Cracker not good enough!")
        f = open("cantcrack.txt","a") #opens file with name of "ip.txt"
        f.write(line+"\n")
    else
	print("Can crack" + line)
	f = open("cancrack.txt","a") #opens file with name of "ip.txt"
        f.write(line+"\n")
f.close()

        
    
            

    

