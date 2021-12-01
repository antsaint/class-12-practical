from random import randint as rn
from random import sample

def password_gen():
    list1 = []
    i = 0
    desired_lenth = int(input("How many digits password you want buddy? "))
    while i < desired_lenth:
        new_num = rn(1, 9)
        list1.append(str(new_num))
        i += 1
 
    password = ''.join(list1)
    print(f'you password is {password}')

def passphrase_gen():
    wordlist_file = open("C:/Users/dell/Desktop/Python Practice/eff_large_wordlist.txt")
    words_list = wordlist_file.read().splitlines()
    desired_lenth = input("How many words do you need in passphrase? ")
    password = sample(words_list, int(desired_lenth))
    displayed_password = '-'.join(password)
    print(f"Your passphrase is {displayed_password}")


def main():
    print("Do you want password or passphrase? ")
    choice = input("Type Word for password and Phrase for passphrase: ")
    if choice.upper() == "WORD":
        password_gen()
    elif choice.upper() == "PHRASE":
        passphrase_gen()
    else:
        print("Type the given options only !")
        main()


main()