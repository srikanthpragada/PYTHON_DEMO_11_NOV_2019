# Print freq of each chars

st = "Java JavaScript"
s = set()


for ch in sorted(st):
    if ch not in s:
        print(ch, st.count(ch))
        s.add(ch)




