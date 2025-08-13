# 🧪 Leviathan Level 6 Writeup

> **Wargame:** Leviathan – OverTheWire   
> **Level:** leviathan6 → leviathan7    
> **Target:** Tìm mật khẩu cho user `leviathan7`

---

## 🖥️ SSH Đăng nhập

```bash
ssh leviathan6@leviathan.labs.overthewire.org -p 2223
Password: szo7HDB88w
```

## 🔎 Cách thực hiện:   
**Payload:**   
```bash
ls
./leviathan6
for i in {0000..9999}; do ./leviathan6 $i;done
cat /etc/leviathan_pass/leviathan7
```

-Khi chạy ```./leviathan6``` được trả về ```usage: ./leviathan6 <4 digit code>```    
==>Brute-force tìm kí tự 4 chữ số khi nào khớp thì xong

### Key: qEs5Io5yM8