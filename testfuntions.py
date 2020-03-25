

#funtion that checks if user inputs a name and returns !


def sayName():
    name = input(" kindly enter your name : ")
    if len(name) > 1:
        print(f'hello {name}')
    else:
        print('hello no name')


sayName()
