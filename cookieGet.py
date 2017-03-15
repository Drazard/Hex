import browser_cookie3, requests, webbrowser, os, time, datetime, re
url = 'data:application/octet-stream;base64,IyBIVFRQIENvb2tpZSBGaWxlIGZvciBkb21haW5zIHJlbGF0ZWQgdG8gaGFja2VyZXhwZXJpZW5jZS5jb20uCiMgRG93bmxvYWRlZCB3aXRoIGNvb2tpZXMudHh0IENocm9tZSBFeHRlbnNpb24gKGh0dHBzOi8vY2hyb21lLmdvb2dsZS5jb20vd2Vic3RvcmUvZGV0YWlsL25qYWJja2lrYXBmcGZmYXBtamdvamNuYmZqb25mamZnKQojIEV4YW1wbGU6ICB3Z2V0IC14IC0tbG9hZC1jb29raWVzIGNvb2tpZXMudHh0IGh0dHBzOi8vbGVnYWN5LmhhY2tlcmV4cGVyaWVuY2UuY29tL2ludGVybmV0P2FjdGlvbj1sb2dpbgojCi5oYWNrZXJleHBlcmllbmNlLmNvbQlUUlVFCS8JRkFMU0UJMTUxMzY1NzMwMQlfX2NmZHVpZAlkNTI5YzU3YzEzNDkzYTg1NDJkM2Q4YzkzMzg1OWE0YmIxNDgyMTIxMjk3Ci5oYWNrZXJleHBlcmllbmNlLmNvbQlUUlVFCS8JRkFMU0UJMAlQSFBTRVNTSUQJZDc0dGhocTJ2aDB1dHM1amlmcmd1a3NlYjQKLmhhY2tlcmV4cGVyaWVuY2UuY29tCVRSVUUJLwlGQUxTRQkxNTIxMTA1NjY3CXBocGJiM182MmRqZV91CTI4NTM1MwouaGFja2VyZXhwZXJpZW5jZS5jb20JVFJVRQkvCUZBTFNFCTE1MjExMDU2NjcJcGhwYmIzXzYyZGplX2sJZjVhZDNmYTc2MmQzMzQ5NwouaGFja2VyZXhwZXJpZW5jZS5jb20JVFJVRQkvCUZBTFNFCTE1MjExMDU2NjcJcGhwYmIzXzYyZGplX3NpZAk5MWU3ZjA1ODVhNDg1ZWNkN2E1ZWQwMTExMTE2YTc1ZQpsZWdhY3kuaGFja2VyZXhwZXJpZW5jZS5jb20JRkFMU0UJLwlGQUxTRQkxNDg5NzQxODQ1CWxvZ2dlZAkxCmxlZ2FjeS5oYWNrZXJleHBlcmllbmNlLmNvbQlGQUxTRQkvCUZBTFNFCTAJaXAtZGF0YQlhJTNBNSUzQSU3QnMlM0ExNCUzQSUyMjk3LjE0Ny4yMTMuMTc5JTIyJTNCcyUzQTE5JTNBJTIyMjAxNy0wMy0xNVQwOSUzQTU4JTNBNDYlMjIlM0JzJTNBMTMlM0ElMjI5Ny4xNTIuMjUxLjUzJTIyJTNCcyUzQTE5JTNBJTIyMjAxNy0wMy0xNVQwOSUzQTU5JTNBMjMlMjIlM0JzJTNBMTQlM0ElMjI5Ny4xOTYuMTQxLjIzOCUyMiUzQnMlM0ExOSUzQSUyMjIwMTctMDMtMTVUMDklM0E1OSUzQTQxJTIyJTNCcyUzQTclM0ElMjIxLjIuMy40JTIyJTNCcyUzQTE5JTNBJTIyMjAxNy0wMy0xNVQxMCUzQTAyJTNBMTElMjIlM0JzJTNBMTIlM0ElMjI5OC43NC4xNDkuODIlMjIlM0JzJTNBMTklM0ElMjIyMDE3LTAzLTE1VDEwJTNBMDIlM0ExNCUyMiUzQiU3RAo='
dlfile = "C:/Users/drazlaptop/Downloads/download"

def save(file, regex):
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
    print("Downloading file...\n")
    time.sleep(2)
    print("Downlaod complete\n")
    dl = open("C:/Users/drazlaptop/Downloads/download", "r")
    download = dl.read()

    t = open("dltemp.txt", "w")
    t.write(str(download))
    t.close()
    t = open("dltemp.txt", "r")

    
    PHPSESSID = ".hackerexperience.com	TRUE	/	FALSE	0	PHPSESSID"
    for line in t:
        if PHPSESSID in line:
            regex = r'(?<=PHPSESSID\t)\w{26}'
            parse = re.findall(regex, line)

            strparse = str(parse)
            f = open("ssid.txt", "w+")
            f.write(strparse)
            print("New SSID:")
            print(parse)
            f.close()

            
                

                               

while True:

    save("ssid.txt","(PHPSESSID\s+\w{26})")
    f = open("ssid.txt", "r")            
    g = f.read()
    fixed = re.findall("\w{26}", g)
    print(fixed)
    time.sleep(1)
    os.remove(dlfile)
    print ("Sleeping for 5 minutes..\n")
    time.sleep(300)
                           



