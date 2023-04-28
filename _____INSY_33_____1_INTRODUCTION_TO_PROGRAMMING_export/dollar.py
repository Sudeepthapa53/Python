#Finding number of dollars, quarters, dimes, pennies for the given amount

amount = float(input("Enter the amount:"))
print(f"Your amount {amount} consists of")

#Number of one dollars

dollars = int(amount)
print(f"{dollars} dollars")
amount= amount-dollars

#Number of quarters in the remaining amount

quarters= int(amount/0.25)
print(f"{quarters} quarters")
amount=amount-(quarters*0.25)

#Number of dimes in the remaining amount

dimes= int(amount/0.10)
print(f"{dimes} dimes")
amount=amount-(dimes * 0.10)

#Number of nickels in the remaining amount

nickels= int(amount/0.05)
print(f"{nickels} nickels")
amount= amount-(nickels * 0.05)

#Number of pennies in the remaining amount
pennies= int(amount/0.01)
print(f"{pennies} pennies")

