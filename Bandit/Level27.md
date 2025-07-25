# 🎯 Bandit Level 27

## 📌 END goal: Tìm key bị giấu
**Describe**: There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo via the port 2220. The password for the user bandit27-git is the same as for the user bandit27.

Clone the repository and find the password for the next level.


```
host: bandit.labs.overthewire.org
port: 2220
username: bandit27
password: upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB

```
---

## ⚙️ Cách thực hiện:
**Payload:**
```bash
ssh -p 2220 bandit27@bandit.labs.overthewire.org
mkdir /tmp/lv27
cd /tmp/lv27
git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
cd repo
ls
cat README
```

### Key: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN

