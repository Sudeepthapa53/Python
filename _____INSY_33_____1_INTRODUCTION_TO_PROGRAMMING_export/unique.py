def main():  #Defining main function
    infile=open("text2.txt","r")  #opening the file in read mode
    print("These are the unique words in the text: ")   
    file_cont=infile.read()  
    words=file_cont.split()  #splits the string to words
    unique_words=set()       #creating an empty set 
    for word in words:       #getting word from list of words within for loop 
        unique_words.add(word) #adds word in the set
    unique_words=set(words)
    for word in unique_words:  
         print(word)          #printing words
    infile.close()            #closing the file
main()
