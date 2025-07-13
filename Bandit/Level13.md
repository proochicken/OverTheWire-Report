# 🎯 Bandit Level 13

## 📌 END goal: Tìm key bị giấu.
**Describe**: The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

```
host: bandit.labs.overthewire.org
port: 2220
username: bandit13
password: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

```
---

## ⚙️ Cách thực hiện:
**Payload:**
```bash
ssh bandit13@bandit.labs.overthewire.org -p 2220
ls
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
cat /etc/bandit_pass/bandit14
```

Ở lab này yêu cầu ta lấy key chứa trong path /etc/bandit_pass/bandit14 chỉ có thể đọc bởi user bandit14.  
Cần kết nối tới bandit14 từ localhost, ở bandit13 ta đã có private_key để có thể kết nối tới bandit14.  

**Lab này cung cấp cho biết được:** Cách hoạt động của cặp khóa private_key và public_key
1. Public_key giống như 1 ổ khóa được server nắm giữ. (đặt trong ~/.ssh/authorized_keys)
2. Private_key giống như chìa khóa, khi đăng nhập ssh dùng private_key đối chiếu với public để xem xét liệu có cho phép đăng nhập không.

### Key: ```MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS```

