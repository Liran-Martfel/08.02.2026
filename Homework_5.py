list_1 = ['HELLO','World','PYTHON','Code']
list_2 = []
for word in list_1:
    if word.isupper():
        list_2.append(word[::-1])
    else:
        list_2.append(word)
print(list_2, end= " ")
