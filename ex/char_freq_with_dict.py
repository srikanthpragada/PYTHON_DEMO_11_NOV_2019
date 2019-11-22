# Print freq of each chars

st = "Java JavaScript"
freq = {}

for ch in st:
    if ch in freq:
        freq[ch] += 1  # increment count
    else:
        freq[ch] = 1   # new char so insert with count 1

for c,cnt in sorted(freq.items()):
    print(c,cnt)








