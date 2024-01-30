with open('day_03.txt','r') as file_obj:
    input_text = file_obj.read()

side_lengths_list = input_text.splitlines()
triangles_list = []
for string in side_lengths_list:
    lengths_list = [int(num) for num in str(string).split()]
    shortest_length = sorted(lengths_list)[0]
    mid_length = sorted(lengths_list)[1]
    longest_length = sorted(lengths_list)[-1]
    if shortest_length + mid_length > longest_length:
        triangles_list.append(lengths_list)
        
print(f'Possible Triangles = {len(triangles_list)}')