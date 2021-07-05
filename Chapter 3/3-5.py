amount = float(input("How many pounds of coffee? "))
cost_fixed = 1.50
sell_pound = 10.50*amount
cost_pound = 0.86*amount

cost_order = cost_fixed + sell_pound + cost_pound

print(cost_order)