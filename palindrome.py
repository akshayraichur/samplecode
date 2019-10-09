# takes an input string from user
name = input('Enter any string to check for palindrome : ')

if name == name[::-1]:  # compares the string with its reverse
    print('{} is a palindrome'.format(name))  # prints the result
else:
    print('{} is not a palindrome'.format(name))

# Contributed By Akshay Raichur
