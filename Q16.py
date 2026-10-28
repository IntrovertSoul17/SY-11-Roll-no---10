
import csv

sales = {}

with open("sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        quantity = int(row[1])
        price = float(row[2])

        amount = quantity * price

        if product not in sales:
            sales[product] = 0

        sales[product] += amount

for product in sales:
    print(product, sales[product])
