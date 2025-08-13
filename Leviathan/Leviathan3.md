# 🧪 Leviathan Level 3 Writeup

> **Wargame:** Leviathan – OverTheWire  
> **Level:** leviathan3 → leviathan4  
> **Target:** Tìm mật khẩu cho user `leviathan4`

---

## 🖥️ SSH Đăng nhập

```bash
ssh leviathan3@leviathan.labs.overthewire.org -p 2223
Password: f0n8h2iWLP
```

## 🔎 Cách thực hiện:   
**Payload:**   
```bash
ls -la
ltrace ./level3
./level3
snlprintf
```
-->Same lv1 easy

### Key: WG1egElCvO