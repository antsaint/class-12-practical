# list slicing

# basket = ['Banana', ['Apples', ['oranges'], 'Blueberries']]

# print(basket[1][1][0]) # first we access basket and then the second object which has index 1 and then its' second object and then the first object

                        
# basket = ['Banana', 'Apples', 'Oranges', 'Blueberries']
# basket.pop(0)
# print(basket)
# basket.pop(2)
# print(basket)
# basket.append('Kiwi')
# print(basket)
# basket.insert(0, 'Apples')
# print(basket)
# print(basket.count('Apples'))
# basket.clear()
# print(basket)


# friends = ["Simon", "Patty", "Joy", "carrie", "Amira", "Chu"]
# new_friend = 'Stanley'
# friends.append(new_friend)
# friends.sort()
# print(friends)

import random
random_number = random.randint(1, 101)
guess = input("Choose a number from 1 to 100: ")
try:
    if int(guess) == random_number:
        print("Bravo")
    else:
        print("No good")
except ValueError:
    print('only integers allowed')
