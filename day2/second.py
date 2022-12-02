points = 0

decrypt_move = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

points_for_move = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
with open("input.txt", 'r') as file:
    for round in file:
        my_move = round[2]
        enemy_move = round[0]
        if enemy_move == "A":
            if my_move == "X":
                points += points_for_move["Z"] + 0
            if my_move == "Y":
                points += points_for_move["X"] + 3
            if my_move == "Z":
                points += points_for_move["Y"] + 6
        if enemy_move == "B":
            if my_move == "X":
                points += points_for_move["X"] + 0
            if my_move == "Y":
                points += points_for_move["Y"] + 3
            if my_move == "Z":
                points += points_for_move["Z"] + 6
        if enemy_move == "C":
            if my_move == "X":
                points += points_for_move["Y"] + 0
            if my_move == "Y":
                points += points_for_move["Z"] + 3
            if my_move == "Z":
                points += points_for_move["X"] + 6

print(points)
