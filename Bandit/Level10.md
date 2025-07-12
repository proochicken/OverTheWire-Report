# 🎯 Bandit Level 10

## 📌 END goal: Tìm key bị giấu.
**Describe**: The password for the next level is stored in the file data.txt, which contains base64 encoded data


```
host: bandit.labs.overthewire.org
port: 2220
username: bandit10
password: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

```
---

## ⚙️ Cách thực hiện:
**Payload:**
```bash
ssh bandit10@bandit.labs.overthewire.org -p 2220
cat data.txt | base64 -d
```

Bài này ta học cách dùng câu lệnh ```base64 -d``` để decode các data chứa trong file data.txt bị encode trước đó

### Key: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr