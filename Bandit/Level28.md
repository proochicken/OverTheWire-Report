# 🎯 Bandit Level 28

## 📌 END goal: Tìm key bị giấu
**Describe**: There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

Clone the repository and find the password for the next level.

```
host: bandit.labs.overthewire.org
port: 2220
username: bandit28
password: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN

```
---

## ⚙️ Cách thực hiện:
**Payload:**
```bash
ssh -p 2220 bandit28@bandit.labs.overthewire.org
git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
ls
cd repo
ls
cat README.md
git log
git diff fb0df1358b1ff146f581651a84bae622353a71c0
```

-Tương tự với lv trước nhưng ở đây khi đọc file ```README.md``` thì password đã bị ẩn đi không thấy được, ta thử soạn ```git log``` 
để xem lịch sử ta thấy có đoạn log ```fix info leak``` vậy tức là ở commit trước đó đã bị lỗi leak info:
```bash
commit 674690a00a0056ab96048f7317b9ec20c057c06b (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Apr 10 14:23:19 2025 +0000

    fix info leak

commit fb0df1358b1ff146f581651a84bae622353a71c0
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Apr 10 14:23:19 2025 +0000

    add missing data

commit a5fdc97aae2c6f0e6c1e722877a100f24bcaaa46
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Apr 10 14:23:19 2025 +0000
```

==>Ta sẽ dùng ```git diff fb0df1358b1ff146f581651a84bae622353a71c0``` để xem commit ban đầu của nó:   
```bash
$ git diff fb0df1358b1ff146f581651a84bae622353a71c0
diff --git a/README.md b/README.md
index d4e3b74..5c6457b 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
+- password: xxxxxxxxxx
```

### Key: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7

