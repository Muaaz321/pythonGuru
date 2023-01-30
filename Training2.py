from main import myfunction

# myfunction(10,"from Training 2")

#userinput = None


# if userinput.isdigit():
#     userinputwithint = int(userinput)
#     calculatedvalue = myfunction(userinputwithint)
#     print(calculatedvalue)
# else:
#     print("This is not a digit . Please enter a valid entry ...")



def validationinput(userinputwithstr):

    try:
        print("Number that entered is >>>>>>>>>>> " + userinputwithstr)
        user_input = int(userinputwithstr) # convert string input in to integer
        if user_input > 0: # check integer is greater than zero
            calculatedvalue = myfunction(user_input) # 
            print(calculatedvalue)
        elif user_input == 0:
            print("You entered a 0 , please enter a valid positive number")
        else:
            print("You entered a negative number , no conversion for you !!! ")
    except ValueError:
        print("Your input is not a valid number ")

userinput = None
while userinput !="exit":
    userinput = input("Hey user number of days , with separator I will convert to hours : \n")
    print(type(userinput.split(",")))
    print(userinput.split(","))
    for num_of_days_element in userinput.split(","): # put the entries in to list
        validationinput(num_of_days_element)
