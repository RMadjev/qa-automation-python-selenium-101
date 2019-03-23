def sum_of_digits(n):
    return sum(int(i) for i in str(abs(n)))


def to_digits(n):
    return [int(i) for i in str(abs(n))]


def to_number(digits):
    res = ''
    for digit in digits:
        res += str(digit)

    return int(res)


def count_vowels(string):
    count = 0

    for letter in string.lower():
        if letter in 'aeiouy':
            count += 1

    return count


def count_consonants(string):
    count = 0
    for letter in string.lower():
        if letter in 'bcdfghjklmnpqrstvwxz':
            count += 1

    return count


def prime_number(number):
    if number == 1:
        return True

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)


def fact_digits(n):
    result = 0
    for digit in to_digits(n):
        result += factorial(digit)

    return result


def fibonacci(n):
    return [get_fibonacci_number(i) for i in range(n)]


def get_fibonacci_number(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    return get_fibonacci_number(n-1) + get_fibonacci_number(n-2)


def fib_number(n):
    string = ''
    for i in range(n):
        string = string + str(get_fibonacci_number(i))
    return int(string)


def palindrome(obj):
    result = ''
    for i in str(obj):
        result = i + result

    return str(obj) == result


def char_histogram(string):
    mydict = {}
    for i in string:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 1

    return mydict
