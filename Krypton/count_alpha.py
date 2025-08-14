freq = {}
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    freq[char] = 0
    
with open('/tmp/tmp.uhtsucCFD5/list_strings', 'r') as f:
    data = f.read()
    
for char in data:
    if char >= 'A' and char <= 'Z':
        freq[char] += 1
        
freq_list = []
for char in freq:
    freq_list.append((char, freq[char]))
    
freq_list.sort(key=lambda x : x[1], reverse=True)

for char, cnt in freq_list:
    print(f"{char} :   {cnt}")