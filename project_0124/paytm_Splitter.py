# Rent, Electricity, Food, persons
rent = int(input("Enter Rent Have to Pay or Paid - "))
food = int(input("Enter Food bills - "))
electricity = int(input("Enter Electricity Spend - "))
electricity_rate = int(input("Enter electicity charge per unit - "))
lownde = int(input("Enter total Persons - "))
electricity_bill = electricity*electricity_rate
output  = (rent+food+electricity_bill)//lownde + (rent+food+electricity_bill)%lownde

print("Each person will pay ",output)