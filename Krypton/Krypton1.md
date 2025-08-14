# 🔑 Krypton Level 1

## 📜 Mô tả đề bài
> The password for level 2 is in the file ‘krypton2’. It is ‘encrypted’ using a simple rotation. It is also in non-standard ciphertext format. When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries. This helps obfuscate any patterns. This file has kept the plain text word boundaries and carried them to the cipher text. Enjoy!

---

## 🧭 Các bước thực hiện
1. **Bước 1**: Login ssh
```bash
ssh krypton1@krypton.labs.overthewire.org -p 2231
KRYPTONISGREAT
```
2. **Bước 2**: Vào folder ```/krypton/krypton1``` đọc file ```README``` thấy nội dung:   
```text
    Welcome to Krypton!

    This game is intended to give hands on experience with cryptography
    and cryptanalysis.  The levels progress from classic ciphers, to modern,
    easy to harder.

    Although there are excellent public tools, like cryptool,to perform
    the simple analysis, we strongly encourage you to try and do these
    without them for now.  We will use them in later excercises.

    ** Please try these levels without cryptool first **


    The first level is easy.  The password for level 2 is in the file 
    'krypton2'.  It is 'encrypted' using a simple rotation called ROT13.  
    It is also in non-standard ciphertext format.  When using alpha characters for
    cipher text it is normal to group the letters into 5 letter clusters, 
    regardless of word boundaries.  This helps obfuscate any patterns.

    This file has kept the plain text word boundaries and carried them to
    the cipher text.

    Enjoy!
```
3. **Bước 3**: Đọc thông tin từ file ```krypton2``` và biết nội dung của nó được mã hóa theo ROT13, giờ ta sẽ có 2 cách làm   
-Cách 1: Lên google tìm các decode tool để giải nó (Như rot13, cyberchef,...)    
-Cách 2: Sử dụng lệnh ```tr``` (translate) để giải mã:   
```bash
cat krypton2| tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
---

## 🧪 Payload (nếu có)
```bash
cd krypton
ls
cd krypton1
ls
cat README
cd ..
cat krypton2 | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

---

## 🧠 Kiến thức cần biết (nếu có)
- Khái niệm/thuật toán: ROT13 là thuật toán dịch chuyển mỗi chữ cái 13 vị trí trong bảng chữ cái (Từ A->N, B->O,...)   
  + Do Tiếng Anh có 26 chữ cái, dịch 13 bước rồi dịch thêm 13 bước nữa sẽ quay lại ban đầu
  + Để giải mã ROT13, ta sẽ sử dụng lệnh ```| tr 'A-Za-z' 'N-ZA-Mn-za-m'```  

- Lệnh hữu ích: ```tr``` là lệnh dịch ký tự theo ánh xạ 1-1.
**Syntax:**   
```bash
tr SET1 SET2
```

+Với SET1 là các ký tự cần thay thế (Ký tự hiện tại)
+SET2 là các ký tự thay thế tương ứng (Sau khi decode)

---

## 🔑 Key
```text
LEVEL TWO PASSWORD ROTTEN
```
