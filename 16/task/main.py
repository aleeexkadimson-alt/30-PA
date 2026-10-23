def get_ticket_total(price, visitors):
    total_price = price * visitors
    return total_price


group_size_1 = int(input("First group total:"))
group_size_2 = int(input("Srcond group total: "))
ticket_price = 5
total_price_1 = get_ticket_total(ticket_price, group_size_1)
total_price_2 = get_ticket_total(ticket_price, group_size_2)

if total_price_1 > total_price_2:
    print("The first group costs more")
else:
    print("The second group costs more")

# First group total: 36
# Second group total: 60
# The second group costs more