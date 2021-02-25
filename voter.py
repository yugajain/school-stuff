    nationality = input("are u indian if yes type y: ")
    age = int(input("age: "))
    if nationality == 'y':
        print('stage 1 passed')  
    else:
        print('stage 1 failed cuz u r not an indian')

    if(age>18):
        print('stage 2 passed you qualified for voter id')
    else:
        print('kiddo u gotta wait for ', 18 - age, 'years')