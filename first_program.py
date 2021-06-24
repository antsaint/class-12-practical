# This program says hello and asks for my name

print("Hello, World!")

my_name = input("What is your name? ") # asks for name
print('It is splendid to meet you ', my_name) # greets the person

length_of_name = len(my_name)
print("The length of your name is: ", length_of_name) # displays the length of name

def age_checker():
    try:
        age = input("What is your age? ") # asks for age
        print('You will be ', str(int(age) + 1) + ' in a year') # see clearly that the variable age is declared int and then string again
    except ValueError as ve:
        print("enter valid integer only bich")
        age_checker()

age_checker()
