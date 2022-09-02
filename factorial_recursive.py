def factorial_recursive(num):
    if num <= 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)


numb = int(input('Please enter a number to calculate its factorial: '))
print('The factorial of %s is %s' % (numb, factorial_recursive(numb)))
