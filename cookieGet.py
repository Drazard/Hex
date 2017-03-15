import browser_cookie3, requests, webbrowser, os, time, datetime, re
url = 'data:application/octet-stream;base64,IyBIVFRQIENvb2tpZSBGaWxlIGZvciBkb21haW5zIHJlbGF0ZWQgdG8gaGFja2VyZXhwZXJpZW5jZS5jb20uCiMgRG93bmxvYWRlZCB3aXRoIGNvb2tpZXMudHh0IENocm9tZSBFeHRlbnNpb24gKGh0dHBzOi8vY2hyb21lLmdvb2dsZS5jb20vd2Vic3RvcmUvZGV0YWlsL25qYWJja2lrYXBmcGZmYXBtamdvamNuYmZqb25mamZnKQojIEV4YW1wbGU6ICB3Z2V0IC14IC0tbG9hZC1jb29raWVzIGNvb2tpZXMudHh0IGh0dHBzOi8vbGVnYWN5LmhhY2tlcmV4cGVyaWVuY2UuY29tL2ludGVybmV0P2FjdGlvbj1sb2dpbgojCi5oYWNrZXJleHBlcmllbmNlLmNvbQlUUlVFCS8JRkFMU0UJMTUxMzY1NzMwMQlfX2NmZHVpZAlkNTI5YzU3YzEzNDkzYTg1NDJkM2Q4YzkzMzg1OWE0YmIxNDgyMTIxMjk3Ci5oYWNrZXJleHBlcmllbmNlLmNvbQlUUlVFCS8JRkFMU0UJMAlQSFBTRVNTSUQJZDc0dGhocTJ2aDB1dHM1amlmcmd1a3NlYjQKLmhhY2tlcmV4cGVyaWVuY2UuY29tCVRSVUUJLwlGQUxTRQkxNTIxMTA1NjY3CXBocGJiM182MmRqZV91CTI4NTM1MwouaGFja2VyZXhwZXJpZW5jZS5jb20JVFJVRQkvCUZBTFNFCTE1MjExMDU2NjcJcGhwYmIzXzYyZGplX2sJZjVhZDNmYTc2MmQzMzQ5NwouaGFja2VyZXhwZXJpZW5jZS5jb20JVFJVRQkvCUZBTFNFCTE1MjExMDU2NjcJcGhwYmIzXzYyZGplX3NpZAk5MWU3ZjA1ODVhNDg1ZWNkN2E1ZWQwMTExMTE2YTc1ZQpsZWdhY3kuaGFja2VyZXhwZXJpZW5jZS5jb20JRkFMU0UJLwlGQUxTRQkxNDg5NzQxODQ1CWxvZ2dlZAkxCmxlZ2FjeS5oYWNrZXJleHBlcmllbmNlLmNvbQlGQUxTRQkvCUZBTFNFCTAJaXAtZGF0YQlhJTNBNSUzQSU3QnMlM0ExNCUzQSUyMjk3LjE0Ny4yMTMuMTc5JTIyJTNCcyUzQTE5JTNBJTIyMjAxNy0wMy0xNVQwOSUzQTU4JTNBNDYlMjIlM0JzJTNBMTMlM0ElMjI5Ny4xNTIuMjUxLjUzJTIyJTNCcyUzQTE5JTNBJTIyMjAxNy0wMy0xNVQwOSUzQTU5JTNBMjMlMjIlM0JzJTNBMTQlM0ElMjI5Ny4xOTYuMTQxLjIzOCUyMiUzQnMlM0ExOSUzQSUyMjIwMTctMDMtMTVUMDklM0E1OSUzQTQxJTIyJTNCcyUzQTclM0ElMjIxLjIuMy40JTIyJTNCcyUzQTE5JTNBJTIyMjAxNy0wMy0xNVQxMCUzQTAyJTNBMTElMjIlM0JzJTNBMTIlM0ElMjI5OC43NC4xNDkuODIlMjIlM0JzJTNBMTklM0ElMjIyMDE3LTAzLTE1VDEwJTNBMDIlM0ExNCUyMiUzQiU3RAo='
dlfile = "C:/Users/drazlaptop/Downloads/download"

def save(file, regex):

    print("file removed")
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
    print("Downloading file...")
    time.sleep(2)
    print("Downlaod complete.")
    dl = open("C:/Users/drazlaptop/Downloads/download", "r")
    download = dl.read()   
    parse = re.findall(regex, download)
    chop = str(parse)
    newSSID = chop[2:28]
    rf = open("ssid.txt", "r")
    ow = open("ssid.txt", "w+")
    oldSSID = rf.read()
    if newSSID not in oldSSID:
        print ("New ID assigned: "+newSSID+". Sleeping for 10 minutes...")
        ow.write(newSSID)
        ow.close()
        rf.close()
        time.sleep
    else:
        print(oldSSID+" Still valid Sleeping for 5 minutes.")
        ow.close()
        rf.close()
        time.sleep(300)

            
                

                               

while True:
    try:
        if os.path.isfile(dlfile):
            os.remove(dlfile)
            save("ssid.txt",r"(?<=PHPSESSID\t)\w{26}")
            time.sleep(1)
            os.remove(dlfile)                     
    except:
        print("ERROR... ")
        os.remove(dlfile)


