number = int(input('enter number: '))
factors = []    # empty list for storing factors
for i in range(2, number):
    if number % i == 0:
        factors.append(i)

if factors == []:
    print('prime number')
else:
    print(f"the factors are {factors}")