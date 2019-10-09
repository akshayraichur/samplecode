name = input('Enter any string to check for palindrome : ')

if name == name[::-1]:
    print('{} is a palindrome'.format(name))
else:
    print('{} is not a palindrome'.format(name))

# Contributed By Akshay Raichur
