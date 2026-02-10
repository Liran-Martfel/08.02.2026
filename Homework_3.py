list_1 = ['Hello','world','Python','java','Code']
list_2 = []
for char in list_1:
    if char.istitle():
        list_2 = [char]
        print(list_2, end= " ")
    else:
        continue