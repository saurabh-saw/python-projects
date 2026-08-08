print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_perc = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

tip = (total_bill * (tip_perc / 100))
bill_per_person = round(((total_bill + tip) / split), 2)

print(f"Each person should pay: ${bill_per_person}")