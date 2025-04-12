from functools import reduce

def compose(*funcs):
    # UZUPEŁNIJ CIAŁO FUNKCJI
    pass

f = compose(lambda x: x + 1, lambda x: x * 2)
print(f(3))  # => 7, bo (3 * 2) + 1
