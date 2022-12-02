
points = 0


decrypt_move = {
    "X" : "A",
    "Y" : "B",
    "Z" : "C"
}

points_for_move = {
    "X" : 1,
    "Y" : 2,
    "Z" :3,
}
with open("input.txt", 'r') as file:
   for round in file:
       points += points_for_move[round[2]]
       my_move = decrypt_move[round[2]]
       enemy_move = round[0]
       if my_move == "A":
           if enemy_move == "A":
               points += 3
           elif enemy_move == "B":
               points+=0
           else:
               points+=6

       if my_move == "B":
           if enemy_move == "A":
               points += 6
           elif enemy_move == "B":
               points += 3
           else:
               points += 0

       if my_move == "C":
           if enemy_move == "A":
               points += 0
           elif enemy_move == "B":
               points += 6
           else:
               points += 3

print(points)