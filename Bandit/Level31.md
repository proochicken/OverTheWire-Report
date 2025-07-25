# 🎯 Bandit Level 31

## 📌 END goal: Tìm key bị giấu
**Describe**: There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.

Clone the repository and find the password for the next level.

```
host: bandit.labs.overthewire.org
port: 2220
username: bandit31
password: fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy
```
---

## ⚙️ Cách thực hiện:
**Payload:**
```bash
ssh -p 2220 bandit31@bandit.labs.overthewire.org
mkdir /tmp/lv31
cd /tmp/lv31
git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
ls
cd repo
ls
cat README.md
rm -r .gitignore
git add key.txt
git commit -m "..."
git push
```

-Ở lab này khi đọc file ```README.md``` có nói:
```bash
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master
```
-Để lấy key thì cần tạo 1 file tên ```key.txt``` với nội dung "May I come in?"    
-Bình thường thì sẽ dùng combo lệnh ```add```, ```commit -m```, ```push``` để đẩy 1 file lên nhưng ở đây có vẻ bị file 
```.gitignore``` cấu hình bỏ qua file ```*.txt```:

```bash
cat .gitignore
*.txt
```

-Giờ xóa nó đi trước khi push file ```key.txt``` lên.

### Key: 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K