#open file with the data
with open('day1_input.txt') as f:
    lines = f.readlines()

#data separation in a array
nums = [str(line.strip()) for line in lines]

#variable to store the highest value and another to compare
most_calories = 0
count = 0

#counting calories until it finds a blank space
for i in nums:
    if i == '':
        count = 0
    else:
        num = int(i)
        count += num
    
    #saving the max calories 
    if count > most_calories:
        most_calories = count

print(most_calories)