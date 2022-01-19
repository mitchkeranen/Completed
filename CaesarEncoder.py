
password = input("Enter the line you would like encoded.")
asc = []
for letter in password:
    asc.append(ord(letter))

for i in range(len(asc)):
    if asc[i] in range(68, 91):
        asc[i] -= 3
    elif asc[i] in range(65, 68):
        asc[i] += 23
    elif asc[i] in range(100, 122):
        asc[i] -= 3
    elif asc[i] in range(97, 100):
        asc[i] += 23

for i in range(len(asc)):
    asc[i] = chr(asc[i])
print(asc)
caesar = ''.join(asc)
print(caesar)



