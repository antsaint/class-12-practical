# sentence = "We \t are the so called \"Vikings\" from the north \n isn\"t that funny"
# print(sentence)

# name = input("enter name : ")
# age = 17

# print(f'Hi {name}. you are {age} years old.')
# import time

# birth_year = input('What year were you born? ')
# age = 2021 - int(birth_year)
# print(f'Your age is {age}.')

user_name = input('enter name: ')
password = input('enter your password: ')
password_length = len(password)
encrypted_password =  '*' * password_length
print(f'hey {user_name}, your password {encrypted_password} the pass is {password_length} digits long')

