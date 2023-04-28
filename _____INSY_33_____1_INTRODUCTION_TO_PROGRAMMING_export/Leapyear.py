year=int(input("Enter a year: "))
#Determining if the entered year is divisible by 100 and 400
if(year%100==0): 
    if(year%400==0):
        Leap_Year=True 
    else:
        Leap_Year=False 
else:
#Determinig if the year is divisible by 4    
    if(year%4==0):
        Leap_Year=True
    else:
        Leap_Year=False 

if(Leap_Year):
    print(" That is a leap year. February has 29 days.")
else:    
    print("That is not a leap year. February has 28 days.")
