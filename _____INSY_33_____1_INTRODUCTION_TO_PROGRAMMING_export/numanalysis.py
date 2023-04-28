number_list=[]  #to create an empty list
for i in range(1,11):  #using for loop with range 1 through 10 
    i=int(input("Enter %d of 10:  "%(i))) 
    number_list.append(i) 
print(number_list) #displays list contents 
low=min(number_list) #finds lowest from the list
high=max(number_list)#finds highest from the list
total=sum(number_list)  #finds total from the list
length=len(number_list)   
avg=float(total/length)   #finds average from the list
print('Low {:.2f}'.format(low)) 
print('High {:.2f}'.format(high))
print('Total {:.2f}'.format(total))
print('Average {:.2f}'.format(avg)) 
#prints the list, lowest, highest, total and average from the list
