meal_cost = float(raw_input("enter meal cost:"))
tip_percent = int(raw_input("enter tip:"))
tax_percent = int(raw_input("enter tax:"))
tip=float(meal_cost*tip_percent)/100
print tip
tax=float(meal_cost*tax_percent)/100
print tax
totalCost=int(meal_cost+tip+tax)
print("The total meal cost is {} dollars.".format(totalCost))
