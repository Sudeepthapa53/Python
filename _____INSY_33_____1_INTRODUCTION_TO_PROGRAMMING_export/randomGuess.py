import random #imports random module
n=random.randint(1,20) #Creating a range from 1 to 20 
while (True):
    guess=int(input("Enter a number between 1 and 20,or 0 to quit:"))
    #generating a number between 1 and 0 
    if((guess>=1)and (guess<=20)):
        if (guess>n):
            print("Too high, try again") #if guess is higher
        elif(guess<n):
            print("Too low,try again") #if guess is lower
        else:
            print("Congratulations! You guessed the right number!") #if the random number is the right guess
    else:
        print("Thanks for playing!") #any number other than 1 to 20 breaks the loop.
        break

    

              
            
