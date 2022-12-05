sum = 0
with open("./input.txt") as file:
    for line in file:
        line = line.strip()
        first_half = line[0:len(line) // 2]
        second_half = line[len(line) // 2:len(line)]
        for x in first_half:
            if x in second_half:
                if x.isupper():
                    sum += ord(x) - ord('A') + 27
                else:
                    sum += ord(x) - ord('a') + 1
                break


print(sum)
