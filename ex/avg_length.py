# Find avg length of given names

st  = input("Enter names sep by , :")
names = st.split(",")
total = 0
for n in names:
    total += len(n)

print("Avg Length : ", total / len(names))




