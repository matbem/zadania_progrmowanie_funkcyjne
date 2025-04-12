from functools import reduce

def to_upper(s): return s.upper()
def strip(s): return s.strip()
def reverse(s): return s[::-1]

def run_pipeline(text, funcs):
    # UZUPEŁNIJ TĘ LINIĘ
    pass

text = "  hello functional world  "
pipeline = [strip, to_upper, reverse]

print(run_pipeline(text, pipeline))  # => DLROW LANOITCNUF OLLEH
