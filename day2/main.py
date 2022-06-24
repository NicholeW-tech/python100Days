print('Welcome to the tip calculator')
bill = round(float(input("What was the total of the bill? $")), 2)
tip = int(input("How much of a tip would you like to give? 10, 12, 15? "))
people = int(input("how many people to split the bill? "))
tip /= 100
tip += 1.0
amount_due = "{:.2f}".format(round(((bill / people) * tip), 2))
print(f"Each person should pay : ${amount_due}")
