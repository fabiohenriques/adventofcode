from string import ascii_letters

#Open and read the input file
with open('day3_input.txt') as f:
    lines = f.readlines()

#data separation in lines
data = [str(line.strip()) for line in lines]

total = 0

for i in data:
    #Find the middle of rucksack 
    #'//' returns an integer instead of a double in '/' 
    half = len(i)//2

    #variable containing the first half
    #'set' function returns a set of all unique characters 
    left = set(i[:half])
    #variable containing the second half
    right = set(i[half:])

    #goes through every single letter
    #assign a number to a letter
    #and increase the number by 1 every time
    #because it starts with 0 we need to "+1"
    for key, char in enumerate(ascii_letters):
        if char in left and char in right:
            total += key + 1

print("total part 1:", total)

#Part 2

x = 3
total_pt2 = 0
#divide data in parts of 3
for i in range(0, len(data), 3):
    elements = data[i:x]
    x += 3

    for key, char in enumerate(ascii_letters):
        if char in elements[0] and char in elements[1] and char in elements[2]:
            total_pt2 += key + 1

print("total part 2:", total_pt2)