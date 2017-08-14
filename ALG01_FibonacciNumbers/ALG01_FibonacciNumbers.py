'''
Given: A positive integer n ≤ 25
Return: The value of Fn
'''

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib())
