with open('day4_input.txt', 'r') as f:
    data = f.read().strip()

sections = data.split('\n')

overlap_q1 = 0

for s in sections:
    s1, s2 = s.split(',')
    s1_start, s1_end = map(int, s1.split('-'))
    s2_start, s2_end = map(int, s2.split('-'))
    if(s1_start <= s2_start and s2_end <= s1_end) or (s2_start <= s1_start and s1_end <= s2_end):
        overlap_q1 += 1

print('Part 1 answer', overlap_q1)