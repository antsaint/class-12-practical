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

# import random
# random_number = random.randint(1, 101)
# guess = input("Choose a number from 1 to 100: ")
# try:
#     if int(guess) == random_number:
#         print("Bravo")
#     else:
#         print("No good")
# except ValueError:
#     print('only integers allowed')

# dictionary = {
#     'basket' : [100, 200, 300],
#     'brie' : 5,
#     'c' : 'hello'
# }

# print(dictionary.get('cd', 100))

# from random import randint
# my_list = [1,2,3,4,5,5]
# print(my_list[randint(0, 6)])
# def gamer():
#     x = 0
#     while x < 5:
#         print(null)
#         x += 1

# my_list = [1,2,3,4]
# count = 0
# for item in my_list:
#     count += item
    
# print(count)
# range()
# pass

# exercise to check for duplicates in the list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)

print(duplicates)

