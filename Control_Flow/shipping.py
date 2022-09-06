weight = input("Enter package weight")
ground_cost = 0
Ground_Ship_Flat = 20

# Ground Shipping

if(weight <= 2):
    ground_cost = 1.50 + Ground_Ship_Flat
elif weight > 2 and weight <= 6:
    ground_cost = 3 + Ground_Ship_Flat
elif weight > 6 and weight <= 10:
    ground_cost  = 4 + Ground_Ship_Flat
elif weight > 10:
    ground_cost = 4.75 + Ground_Ship_Flat

# Ground Shipping Premium

Premium_Flat_Rate = 125
premium_cost = 0

if(weight <= 2):
    premium_cost = 4.50 + Premium_Flat_Rate
elif weight > 2 and weight <= 6:
    premium_cost = 9 + Premium_Flat_Rate
elif weight > 6 and weight <= 10:
    premium_cost  = 12 + Premium_Flat_Rate
elif weight > 10:
    premium_cost = 4.75 + Ground_Ship_Flat

