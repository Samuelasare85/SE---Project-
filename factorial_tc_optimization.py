def factorial_tc_optimization(num, a=1):
    if num <= 1:
        return a
    else:
        return factorial_tc_optimization(num - 1, num * a)


numb = int(input('Enter a number to calculate its factorial: '))
print('The factorial of %s is %s' % (numb, factorial_tc_optimization(numb)))
