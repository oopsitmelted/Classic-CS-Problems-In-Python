import sys


def findInterleavings(X, Y, interleavings, curr=''):
    if not X and not Y:
        interleavings.add(curr)
        return

    if X:
        findInterleavings(X[1:], Y, interleavings, curr + X[0])

    if Y:
        findInterleavings(X, Y[1:], interleavings, curr + Y[0])

    return interleavings

def findAllInterleavings(X, Y):
    interleavings = set()

    if not X and not Y:
        return interleavings

    findInterleavings(X, Y, interleavings)
    return interleavings

def findMaxProduct(set, maximum):
    product = 1

    for i in set:
        product = product * i

    if set:
        maximum = max(maximum, product)

    return maximum

def findPowerSet(nums, s, n, maximum):

    if n == 0:
        return findMaxProduct(s, maximum)

    s.append(nums[n - 1])
    maximum = findPowerSet(nums, s, n - 1, maximum)
    s.pop()
    return findPowerSet(nums, s, n - 1, maximum)

def maxProductSubset(nums):
    s = []
    n = len(nums)

    return findPowerSet(nums, s, n, -sys.maxsize)

def split(num, result):
    if num > 0:
        split(num // 10, result)
        result.append(num % 10)

def addElements(x, y, result):
    i = 0

    while i < len(x) and i < len(y):
        sum = x[i] + y[i]
        split(sum, result)
        i = i + 1

    while i < len(x):
        split(x[i], result)
        i = i + 1

    while i < len(y):
        split(y[i], result)
        i = i + 1

if __name__ == '__main__':
    X = 'ABC'
    Y = 'ACB'

    interleavings = findAllInterleavings(X, Y)
    print(interleavings)
    nums = [-6, 4, -5, 8, -10, 0, 8]
    print(maxProductSubset(nums))
    x = [10, 5, 34, 89, 2, 10, 3]
    y = [2, 46, 10, 5, 99]
    r = []
    addElements(x, y, r)
    print(r)
