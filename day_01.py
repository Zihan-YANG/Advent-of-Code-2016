# Starting condition
position_x, position_y = 0, 0
current_direction = 'N'
# Direction map dic
direction_map = {
'N': {'L':'W','R':'E'},
'E': {'L':'N','R':'S'},
'S': {'L':'E','R':'W'},
'W': {'L':'S','R':'N'}
}

# Input
file_obj = open('day_01.txt', 'r')
input_text = file_obj.read()
file_obj.close()

for instruction in input_text.split(', '):
    left_right = instruction[0]
    step_text = instruction[1:]
    steps = int(step_text)
    new_direction = direction_map[current_direction][left_right]
    if new_direction == 'N':
        position_y = position_y + steps 
    elif new_direction == 'S':
        position_y = position_y - steps
    elif new_direction == 'E':
        position_x = position_x + steps
    elif new_direction == 'W':
        position_x = position_x - steps
    else:
        print(f'Wrong direction: {new_direction}')
    # Record the new direction
    current_direction = new_direction

# Print result
print(f'Ending position: ({position_x}, {position_y})')
print(f'Distance: {abs(position_x) + abs(position_y)}')