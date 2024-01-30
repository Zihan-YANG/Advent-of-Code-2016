keypad = [
    [None,None,'D',None,None],
    [None,'A','B','C',None],
    ['5','6','7','8','9'],
    [None,'2','3','4',None],
    [None,None,'1',None,None]
]

coordinate_map = {
    'U':(0,1),
    'D':(0,-1),
    'L':(-1,0),
    'R':(1,0)
}

with open('day_02.txt','r') as file_obj:
    input_text = file_obj.read()
    
current_position = (0,2)
bathroom_code = ''

for instruction in input_text.splitlines():
    for letter in instruction:
        x_adjustment,y_adjustment = coordinate_map[letter]
        x_position = current_position[0] + x_adjustment
        y_position = current_position[1] + y_adjustment
        
        x_position = min(max(x_position,0),4)
        y_position = min(max(y_position,0),4)
        
        if keypad[y_position][x_position] != None:
            current_position = (x_position,y_position)
        
    bathroom_code = bathroom_code + keypad[current_position[1]][current_position[0]]

print(f'bathroom code: {bathroom_code}')