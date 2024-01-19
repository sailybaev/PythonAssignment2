input_list = [1, 2, 2, 3, 4, 4, 5, 5]
sett = set(input_list)

for i in sett:
    cal = 0
    for j in input_list:
        if i == j:
            cal+=1
    if cal == 1:
        print(i , end=" ")
