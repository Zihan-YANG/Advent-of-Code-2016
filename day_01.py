# Starting condition
position_x, position_y = 0, 0
current_direction = 'N'
visited_position = []
ebhq_position = False 
# Direction map dic
direction_map = {
'N': {'L':'W','R':'E'},
'E': {'L':'N','R':'S'},
'S': {'L':'E','R':'W'},
'W': {'L':'S','R':'N'}
}
# Coordinate map dic
coordicate_map = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
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
    coordinate_adjustment = coordicate_map[new_direction]

    for step in range(steps):
        position_x = position_x + coordinate_adjustment[0]
        position_y = position_y + coordinate_adjustment[1]
        if (position_x, position_y) in visited_position:
            ebhq_position = True
            break
        visited_position.append((position_x, position_y))
    if ebhq_position:
        break 
    current_direction = new_direction
   
# Print result
print(f'Ending position: ({position_x}, {position_y})')
print(f'Distance: {abs(position_x) + abs(position_y)}')