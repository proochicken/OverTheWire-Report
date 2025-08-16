# Natas Level 3

## 🔑 Mục tiêu
Tìm password cho level tiếp theo.

**URL: http://natas3.natas.labs.overthewire.org**     
**Credential: natas:*3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH***

## 🛠️ Các bước thực hiện
1. Tổng quan trang web:
![alt text](Image/Natas3.png)

1. Check source code thì thấy 1 comment:    
```bash
<!-- No more information leaks!! Not even Google will find it this time... -->
```

==> Ta sẽ truy cập vào ```/robots.txt```, ta sẽ thấy 1 folder ```s3cr3t``` trong này, redirect tới đó và lấy password từ file user.txt.     

## Kiến thức cần biết:
-```robots.txt``` là file hướng dẫn web crawler (bot tìm kiếm như Google, Bingbot,...) có thể truy cập hoặc không được truy cập phần nào của page.    

## 📌 Key: ```QryZXc2e0zahULdHrtHxzyYkj59kUxLQ```