# 🧪 Leviathan Level 4 Writeup

> **Wargame:** Leviathan – OverTheWire  
> **Level:** leviathan4 → leviathan5  
> **Target:** Tìm mật khẩu cho user `leviathan5`

---

## 🖥️ SSH Đăng nhập

```bash
ssh leviathan4@leviathan.labs.overthewire.org -p 2223
Password: WG1egElCvO
```

## 🔎 Cách thực hiện:   
**Payload:**   
```bash
ls -la
cd .trash
ls -la
./bin
```

-Có 1 execute file với quyền SUID có 1 dãy các chuỗi binary, decode nó về dạng ASCII   

### Key: 0dyxT7F4QD