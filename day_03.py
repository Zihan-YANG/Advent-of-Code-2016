with open('day_03.txt','r') as file_obj:
    input_text = file_obj.read()

side_lengths_list = input_text.splitlines()
lengths_list = []
column_1 = [] 
column_2 = []
column_3 = []
triangle_1 = []
triangle_2 = []
triangle_3 = []
possible_list = []

for string in side_lengths_list:
    lengths_x = [int(num) for num in str(string).split()]
    lengths_list.append(lengths_x)
for list in lengths_list:
    column_1.append(int(list[0]))
    column_2.append(int(list[1]))
    column_3.append(int(list[-1]))
    
for i in range(0,len(column_1),3):
    triangle_1.append(column_1[i:i+3])

    
for i in range(0,len(column_3),3):
    triangle_2.append(column_2[i:i+3])
    
for i in range(0,len(column_3),3):
    triangle_3.append(column_3[i:i+3])
    
triangle_list = triangle_1 + triangle_2 + triangle_3
for tiangle in triangle_list:
    side_s = int(sorted(tiangle)[0])
    side_m = int(sorted(tiangle)[1])
    side_l = int(sorted(tiangle)[-1])
    if side_s + side_m > side_l:
        possible_list.append(tiangle)
    
print(f'Possible Triangles = {len(possible_list)}')