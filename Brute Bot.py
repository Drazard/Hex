import subprocess
import webbrowser
import sys
import requests
import time

SSID = input("Session ID: ")
cookies = dict(PHPSESSID=str(SSID))
f = open("bruteips.txt")
for line in f:
    time.sleep(1)
    url = "https://legacy.hackerexperience.com/internet?action=hack&method=bf&ip=" + line
    req = requests.get(url, cookies=cookies)
    result = req.text

    if "your cracker is not good enough." in result:
        print("Cracker not good enough!")
        f = open("cantcrack.txt","a")
        f.write(line+" \n")
            
    elif "This IP is already on your hacked database" in result:
        print(line+" Already hacked!")
        f = open("alreadyhacked.txt", "a")
        f.write(line+" \n")
        

    elif "This ip does not exists." in result:
        print(line+" Does not exist!")
        f = open("doesnotexist.txt", "a")
        f.write(line+" \n")

    else:

                
        print("logging: "+line)

        if sys.platform=='win32':
            os.startfile(url)
            time.sleep(3)

        elif sys.platform=='darwin':
            subprocess.Popen(['open', url])
            time.sleep(3)

        else:

            try:
                subprocess.Popen(['xdg-open', url])
                time.sleep(3)
            except OSError:
                print ('Please open a browser on: '+url)


f.close()

        
    
            

    

