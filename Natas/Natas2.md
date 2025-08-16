# Natas Level 2

## 🔑 Mục tiêu
Tìm password cho level tiếp theo.

**URL: http://natas2.natas.labs.overthewire.org**     
**Credential: natas2:*TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI***

## 🛠️ Các bước thực hiện
1. Tổng quan trang web:
![alt text](Image/Natas2.png)

2. Khi check source code, ta thấy 1 link tới 1 image file:    x

```bash
<img src="files/pixel.png">
```

-Thử xóa filename đi tới link ```http://natas2.natas.labs.overthewire.org/files/files``` để lấy nội dung của directory này.    
-Ta tìm thấy password cho natas3 ở file ```user.txt```

```bash
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
eve:zo4mJWyNj2
mallory:9urtcpzBmH
```

## 📌 Key: ```3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH```