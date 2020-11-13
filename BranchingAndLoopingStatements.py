# printing hello world on screen
print('hello world')


# Branching statements

# Simple_if statement
if True:
    print('hello world')


# if-else statement(condition True)
i = 10
if i == 10:
    print('hello world')
else:
    print('Sorry')


# if-else statement(condition False)
i = 1
if i == 10:
    print('hello world')
else:
    print('sorry')


# nested-if statement
i = 5
if i <= 10:
    print('less than or equal to 10')
    if i == 10:
        print('equal to 10')
        if True:
                print('hello world')


# if-elif statement

inp = int(input('Enter an integer: '))
if inp < 0:
    print('Negative integer')
elif inp > 0:
    print('Positive integer')
elif inp == 0:
    print('Zero')


# nested if-else statement
inp = int(input("Enter an integer: "))
if inp % 2 == 0:
    print('Even')
    if inp < 0:
        print('Negative integer')
    elif inp > 0:
        print('Positive integer')
    elif inp == 0:
        print('Zero')
else:
    print('Odd')
    if inp < 0:
        print('Negative integer')
    elif inp > 0:
        print('Positive integer')
    elif inp == 0:
        print('Zero')


# Looping statements

# While loop
i=5
while i>1:
    print('value: %d'%i)
    i-=1


# While loop with else
j=10
while j == 5:
    print('while block')
    print('value: %d'%j)
    j-=1
else:
    print('else block\nValue is greater than 5')
    print('value: %d'%j)

