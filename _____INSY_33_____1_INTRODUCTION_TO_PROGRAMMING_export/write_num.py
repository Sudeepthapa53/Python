def main():
    file = open("num_list.txt",'w') #open file as num_list in write mode
    for i in range(1,101):      #for loop for range 1 through 101 into file
        file.write(str(i)+"\n")
    print("Successfully created num_list.txt in .py file")
    file.close() #close the file
main()

