sum = 0
letters = []
file = open("input.txt")
lines = file.readlines()
file.close()
for i in range(0,len(lines), 3):
    for x in lines[i].strip():
        if x in lines[i + 1].strip() and x in lines[i + 2].strip():
            letters.append(x)
            break

for x in letters:
    if x.isupper():
        sum += ord(x) - ord('A') + 27
    else:
        sum += ord(x) - ord('a') + 1

print(sum)
