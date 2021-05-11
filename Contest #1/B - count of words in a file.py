c = 1
file = input()
for i in range(len(file)):
    if file[i] == ' ':
        c += 1
print(c)
