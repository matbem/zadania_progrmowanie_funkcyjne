def apply_tax(price_list, tax_rate):
    return [round(p * (1 + tax_rate), 2) for p in price_list]

prices = [100, 200, 300]
with_tax = apply_tax(prices, 0.23)

print("Original:", prices)
print("With tax:", with_tax)
