# 🎯 Bandit Level 22

## 📌 END goal: Tìm key bị giấu
**Describe**: A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.


```
host: bandit.labs.overthewire.org
port: 2220
username: bandit22
password: tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q

```
---

## ⚙️ Cách thực hiện:
**Payload:**
```bash
ssh -p 2220 bandit22@bandit.labs.overthewire.org
cd /etc/cron.d
ls
cat cronjob_bandit23
cat /usr/bin/cronjob_bandit23.sh
./cronjob_bandit23.sh
cat ../../../tmp/8169b67bd894ddbb4412f91573b38db3
```

-Tương tự với Level21, ở Level này khi đọc file chứa script:  
```bash
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

Ở script này sẽ lấy biến ```myname``` là ```bandit22``` sau đó biến ```mytarget``` sẽ có dạng ```I am user bandit22``` và được mã hóa md5

Lệnh ```cut -d ' ' -f 1``` sẽ tách chuỗi theo dấu cách và lấy chuỗi đầu tiên.   

-Chạy thử script:   
![alt text](./image/Level22.png)

==>Vậy để tìm file chứa key cho Level23, ta đổi từ ```bandit22``` thành ```bandit23```:   
```bash
echo I am user bandit23 | md5sum | cut -d ' ' -f 1
```

-Ta đọc file ```/tmp/8ca319486bfbbc3663ea0fbe81326349``` có được key

### Key: 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga