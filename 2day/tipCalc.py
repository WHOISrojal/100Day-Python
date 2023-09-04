print('Welcome to the tip calculator')
bill = float(input("What was the total bill?"))
split = int(input("How many people to split the bill?"))
tip = float(input("What percentage tip would you like to give 10, 12 or 15?"))
tippercent = tip/100
tot_tip = bill * tippercent
tip_amt = bill + tot_tip
amt_split = bill / split
print("Each person should pay:",amt_split)
