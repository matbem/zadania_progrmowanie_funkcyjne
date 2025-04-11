def compose(*functions):
    def composed(x):
        for f in reversed(functions):
            x = f(x)
        return x
    return composed

def double(x): return x * 2
def square(x): return x ** 2
def increment(x): return x + 1

pipeline = compose(increment, square, double)  # (2x)^2 + 1
print(pipeline(3))  # => (2*3)^2 + 1 = 36 + 1 = 37
