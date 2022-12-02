#opening the data
with open('day2_input.txt') as f:
    lines = f.readlines()

#transforming the data in a list
data = [str(line.strip()) for line in lines]

#all possible outcomes and how many points i get for each
outcomes = {
    "A X":4, "A Y":8, "A Z":3,
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6
}

#variable to count all the points i won
total_points = 0
#loop to count all rounds in the data file 
for round in data:
    total_points += outcomes[round]

#print total points won
print(total_points)