list_ = ['HELLO', 'World','PYTHON','code','TEST']
list_2 = []
for word in list_:
    if word.isupper():
        list_2 = [word]
        print(list_2, end= " ")
    else:
        continue