def is_prime(number):
    if(number == 1):
        return False 
    for x in range(2,number):
        if number%x == 0: #numbers divided by value x
            return False
    return True #returns false and true accordingly 

def main():
    print("number is prime")
    print("------------------------")

    for i in range(1,11): #for range 1 to 10 for the loop
        if is_prime(i):
            print(i, "prime")
        else:
            print(i, "not prime") 

main()
