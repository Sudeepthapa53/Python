class Person: #creating a class named Person
    def __init__(self, name, address, telephone_number):
        #initializing constructor for name,address and telephone number attributes
        self.name = name
        self.address = address
        self.telephone_number = telephone_number
    
class Customer(Person): #creating a subclass of the Person class
    def __init__(self, name, address, telephone_number, customer_number, mailing_list):
        #inititalizing class constructor 
        Person.__init__(self,name, address, telephone_number)
        self.customer_number = customer_number
        self.mailing_list = mailing_list
#taking inputs from the user
name=input("Enter the name:")
address=input("Enter the address:")
telephone_number=input("Enter the phone number:")
customer_number=input("Enter the customer number:")
mailing_list=input("Does the customer wish to be on the mailing list?(Yes/No)")
if mailing_list=="yes":
   list = True
else:
   list = False
obj = Customer(name,address,telephone_number,customer_number, list)
#variable object accepting inputs
print("\nCustomer Information:")
print("Name:" + obj.name)
print("Address:"+obj.address)
print("Phone number:" +str(obj.telephone_number))
print("Customer number:" +str(obj.customer_number))
print("On Mailing List:" +str(obj.mailing_list))
#printing all the values 
                 
    
        
