def main():   #Defining main
    upper=0
    lower=0
    digit=0
    space=0  #initializing all the countings
    file=open("text.txt","r") #opening the file 
    for i in file.read():     
        if(i.isupper()):
            upper+=1
        elif(i.islower()):
            lower+=1
        elif(i.isdigit()):
            digit+=1
        elif(i.isspace()):
            space+=1
    #counting uppercase, lowercase letters, digits, spaces
    file.close()        #closing the file
    print("Uppercase letters:",upper)
    print("Lowercase letters:",lower)
    print("Digits:",digit)
    print("Spaces:",space)
    #Displaying total uppercase, lowercase letters, digits, spaces
main()
