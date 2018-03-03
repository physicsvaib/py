meal_cost = 12
tip_percent = 20
tax_percent = 8
tip=meal_cost*tip_percent/100
tax=meal_cost*tax_percent/100
x=meal_cost+tip+tax
y=5
print("The total meal cost is {a} {b} dollars.".format(a=round(x),b=(y)))