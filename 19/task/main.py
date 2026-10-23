def get_print_cost(pages, copies, price=0.1):
    total_price = pages * price * copies

    return total_price


default_cost = get_print_cost(100, 1)
print(f"Default printing cost: {default_cost}")

custom_cost = get_print_cost(10,1,0.2)
print(f"Custom printing cost: {custom_cost}")

# Default printing cost: 3.0
# Custom printing cost: 6.0