def digitsList(number):
    if number == 0:
        return [0]

    digits = []

    number = number

    while number != 0:
        digits.append(number % 10)
        number //= 10
    
    digits.reverse()
    return digits

def hasTwoSameAdjacentDigits(digits):
    for i in range(0, len(digits) - 1):
        if digits[i] == digits[i + 1]:
            return True
    
    return False

def hasNonDecreasingDigits(digits):
    for i in range(0, len(digits) - 1):
        if digits[i + 1] < digits[i]:
            return False

    return True

def part1():
    def meetsCriteria(number):
        digits = digitsList(number)
        return hasTwoSameAdjacentDigits(digits) and hasNonDecreasingDigits(digits)

    min = 353096
    max = 843212

    counter = 0

    for number in range(min, max + 1):
        if meetsCriteria(number):
            counter += 1

    print(counter)

part1()

# Part 2

def hasExactlyTwoSameAdjacentMatchingDigits(digits):
    matchCount = 0

    for i in range(0, len(digits) - 1):
        if digits[i] == digits[i + 1]:
            matchCount += 1
        elif matchCount == 1:
            return True
        else: 
            matchCount = 0
    
    return matchCount == 1

def part2():
    def meetsCriteria(number):
        digits = digitsList(number)
        return hasExactlyTwoSameAdjacentMatchingDigits(digits) and hasNonDecreasingDigits(digits)

    min = 353096
    max = 843212

    counter = 0

    for number in range(min, max + 1):
        if meetsCriteria(number):
            counter += 1

    print(counter)

part2()