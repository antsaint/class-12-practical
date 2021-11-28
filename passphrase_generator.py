# We import sample so as to get desired number of random items from our list.
from random import sample

# Then we open the .txt file which contains large number of words
wordlist_file = open("C:/Users/dell/Desktop/Python Practice/eff_large_wordlist.txt")

# We spit out the words into a list
words_list = wordlist_file.read().splitlines()

# We ask for desired length of passphrase

desired_lenth = input("How many words do you need in passphrase? ")

# Finally using sample function we take desired number of random words from our list
password = sample(words_list, int(desired_lenth))

# We join the words so as to make password readable
displayed_password = '-'.join(password)

# Finally we print it.
print(f"Your passphrase is {displayed_password}")
