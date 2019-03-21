def num_add(a, b):
    return a + b


def num_sub(a, b):
    return a - b


def num_mul(a, b):
    return a * b


def num_div(a, b):
    return a / b


def num_floor(a, b):
    return a // b


def num_rem(a, b):
    return a % b


IS_TRUE = True

IS_FALSE = False


PANCAKE_INGREDIENTS = {
    'flour': 2,
    'eggs': 4,
    'milk': 200,
    'butter': False,
    'salt': 0.001
}


def ingredient_exists(ingr, dict):
    return ingr in dict


def fatten_pancakes(dict):
    new_ingredients = dict.copy()
    new_ingredients['eggs'] = 6
    new_ingredients['butter'] = True

    return new_ingredients


def add_sugar(dict):
    new_ingredients = dict.copy()
    new_ingredients['sugar'] = 100

    return new_ingredients


def remove_salt(dict):
    new_ingredients = dict.copy()
    if 'salt' in new_ingredients:
        del new_ingredients['salt']

    return new_ingredients


FIBONACCI_NUMBERS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


def add_fibonacci(lst):
    lst.append(lst[-1] + lst[-2])

    return lst


def fib_exists(lst, n):
    return n in lst


def which_fib(lst, n):
    if n in lst:
        index = lst.index(n)
        return index + 1
    raise ValueError

