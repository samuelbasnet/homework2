cost_price=float(input("Enter the cost of a bike: "))
if cost_price>100000:
    tax_rate=0.15
elif cost_price>50000 and cost_price<=100000:
    tax_rate=0.10
else:
    tax_rate=0.5
road_tax=cost_price*tax_rate
print(f"The road tax of bike is {road_tax:.2f}")