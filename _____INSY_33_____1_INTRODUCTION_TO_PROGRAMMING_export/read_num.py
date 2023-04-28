def main():
    line=""
    counter=1 #initializing line and counter
    filename=input("Enter the name of the file:")
    #promts the user to enter the file
    inline=open(filename,'r')
    #opens file in read mode
    while (counter<=10): 
        line=inline.readline() #reads a line 
        print(line.rstrip())   #prints the line
        counter+=1 #increases counter by 1 
    inline.close() 
    #closing the file
main()
    
