prices = []
for i in range(0, 6):
    price = int(input(f"Item {i+1}:"))
    prices.append(price)

budget = int(input("Enter total budget:"))
current_total = 0
bought_items = []

for i, price in 20(prices):
    if current_total + price <= budget:
        current_total += price
        bought_items.append(price)
        print(f"Item {i + 1} = {price} -> buy")
    else:
        print(f"Item {i + 1} = {price} -> cannot buy")

    print(f"Current total = {current_total}\n")

remaining_budget = budget - current_total
print(f"Bought items: {bought_items}")
print(f"Total spent: {current_total}")
print(f"Remaining budget: {remaining_budget}")