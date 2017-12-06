'''
--- Part Two ---

Now, the jumps are even stranger: after each jump, if the offset was three or more,
instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps,
and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?

'''

def solution(input_list):
    ''' store previous pointer, increment every step count, move current pointer to new position.
        do while current pointer does not exceed or equal length of the list
    '''
    i = 0
    num_steps = 0
    length = len(input_list)
    while not i >= length:
        num_steps += 1
        prev = i
        i += input_list[i]
        if input_list[prev] >= 3:
            input_list[prev] -= 1
        else:
            input_list[prev] += 1
    return num_steps

with open('p5.txt', 'r') as f:
    data = f.read()
    data_list = [int(i) for i in data.split('\n')]
    print(solution(data_list))
