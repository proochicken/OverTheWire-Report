import string

ciphertext = "KSVVWBGSJDSVSISVXBMNYQUUKBNWCUAANMJS"
#english_freq = "ETAOINSRHLDCUMFPGWYBVKXJQZ"
modified_freq = "EQTSORINHCLDUPMFWGYBKVXQJZ"
cipher_freq = "SQJUBNCGDZVWMYTXKELAFIOHRP"

key = ''
for i in ciphertext:
    l = cipher_freq.index(i)
    key += modified_freq[l]
    
print(key)