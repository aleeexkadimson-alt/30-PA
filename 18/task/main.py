def get_order_total(amount, delivery=5):
    total = amount + delivery
    return total

with_delivary = get_order_total(40)
print(f"Standart delivary total: {with_delivary}")
without_delivary = get_order_total(40,0)
print(f"Free delivery total: {without_delivary}")
# Standard delivery total: 45
# Free delivery total: 40