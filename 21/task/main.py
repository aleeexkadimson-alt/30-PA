def get_in_stock(stocks):
    new_list = list ()
    for i in range(len(stocks)):
        if stocks[i] > 0:
            new_list.append(stocks[i])

    return new_list

some_stocks = In stock: [5, 3, 5]
Original stocks: [5, 0, -2, 3, 5]










# In stock: [5, 3, 5]
# Original stocks: [5, 0, -2, 3, 5]