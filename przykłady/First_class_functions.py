def to_upper(s): return s.upper()
def strip_whitespace(s): return s.strip()
def reverse(s): return s[::-1]

def pipeline(data, funcs):
    return reduce(lambda acc, f: f(acc), funcs, data)

from functools import reduce
text = "  funkcyjne programowanie  "
functions = [strip_whitespace, to_upper, reverse]

print(pipeline(text, functions))
