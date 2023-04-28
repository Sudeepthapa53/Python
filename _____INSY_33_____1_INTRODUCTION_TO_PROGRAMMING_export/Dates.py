#Determining if the date is magic or not

month = int(input("Enter a value for month between 1 and 12:"))
day = int(input("Enter a value for day between 1 and 31:"))
year = int(input("Enter a value for year between 0 and 99:"))
if month * day == year:
    print("This is a magic date")
else:
    print("This is not a magic date")
    
#when the multiplication of month and day equals the year, it is considered to be a magic date
