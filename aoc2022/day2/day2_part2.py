#opening the data
with open('day2_input.txt') as f:
    lines = f.readlines()

#transforming the data in a list
data = [str(line.strip()) for line in lines]

#all possible outcomes and how many points i get for each
#edited to indicated "top secret" formula
top_secret_outcomes = {
    "A X":3 , "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7
}

#variable to count all the points i won
total_points = 0
#loop to count all rounds in the data file 
for round in data:
    total_points += top_secret_outcomes[round]

#print total points won
print(total_points)