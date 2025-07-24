# 🎯 Bandit Level 15

## 📌 END goal: Tìm key bị giấu.
**Describe**: The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

```
host: bandit.labs.overthewire.org
port: 2220
username: bandit15
password: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

```
---

## ⚙️ Cách thực hiện:
**Payload:**
```bash
ssh bandit15@bandit.labs.overthewire.org -p 2220
openssl s_client -connect localhost:30001
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```
-Bước 1: Gửi mật khẩu đến cổng 30001 qua SSL:
```bash
openssl s_client -connect localhost:30001
```   
Lệnh trên tạo kết nối SSL đến localhost, giúp kiểm tra máy chủ và gửi dữ liệu an toàn.

-Bước 2: Nhập password đã lấy được của level trước đó.

### Key: kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx