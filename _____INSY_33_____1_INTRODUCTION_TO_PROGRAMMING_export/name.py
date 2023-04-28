def main(): #defining main function
    full_name=input("Enter your full name:")  #prompting user to enter full name
    first_name, middle_name, last_name= full_name.split() #spit function splits the full name
    print(first_name[0].upper()+('.'), middle_name[0].upper()+('.'), last_name[0].upper()+('.'))
    #upper function capitalizes the first, second and last name.
    #[0] helps to get first character of a string
    #('.') separates initials of the full name
main()
