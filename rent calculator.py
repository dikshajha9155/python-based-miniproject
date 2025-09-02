# Total rent
## Input we need from the user 
# Total food for snacking
 # charge for rent 
#person living in room/flat


## output
#Total amount you've to pay is

rent  = int(input("Enter your hostel/flat rent = "))
food  = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of ellectricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("enter the number of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit
output = (food + rent + total_bill) // persons

print("Each persons will pay = ", output) 