
with open("input.txt", 'r') as file:
    current_calories = 0
    calories_amounts = []

    for line in file:
        if line == "\n":
            calories_amounts.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line)
            if current_calories > biggest_calories_amount:
                biggest_calories_amount = current_calories

    calories_amounts.sort()

    print(calories_amounts[-1])
    print(sum(calories_amounts[-1:-4:-1]))