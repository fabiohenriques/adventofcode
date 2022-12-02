#open file with the data
with open('day1_input.txt') as f:
    lines = f.readlines()

#data separation in a array
nums = [str(line.strip()) for line in lines]

#variable to count each elve calories and another to store all the elves calories
every_elves_calories = []
count = 0

#counting calories until it finds a blank space
#when it finds a blank space store the total calories for that elve
#and reset the count to the next one
for i in nums:
    if i == '':
        every_elves_calories.append(count)
        count = 0
    else:
        count += int(i)

#finding the highest("max") number in the list 
print(max(every_elves_calories))

#data = sorted(data)
#print(data[-1]+data[-2]+data[-3])