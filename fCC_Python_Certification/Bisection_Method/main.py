

def square_root_bisection(number, tolerance=0.01, iterations=10):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if number in (0, 1):
        print(f'The square root of {number} is {number}')
        return number
    root = -1
    lower = 0
    upper = number if number > 1 else 1
    for i in range(iterations):
        middle = (upper + lower) / 2
        if (upper - lower) <= tolerance:
            root = middle
            print(f'The square root of {number} is approximately {root}')
            return root
        if middle ** 2 > number:
            upper = middle
        else:
            lower = middle
    print(f'Failed to converge within {iterations} iterations')

print(square_root_bisection(0))
print(square_root_bisection(1))
print(square_root_bisection(9, 0.000001, 1000))
print(square_root_bisection(0.001, 1e-7, 50))
print(square_root_bisection(81, 1e-3, 50))
print(square_root_bisection(0.25, 1e-7, 50))
print(square_root_bisection(225, 1e-7, 10))
        
square_root_bisection(0.25, 1e-7, 50)
