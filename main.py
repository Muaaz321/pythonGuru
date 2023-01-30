# print(200)
# print("This is a text")
# print(-445342)
# print(45.53432525)
# print(20 * 24 * 60)

calculations = 24
name_of_unit = "hours"


# print("20 days are "+ str(50)+" minutes")
# print(f"20 days are {50} minutes") # new latest update
# print(f"20 days are {20 * calculations_to_units } {name_of_unit}")
# print(f"35 days are {35 * 24 * 60} minutes")
# print(f"35 days are {35 * calculations_to_units} seconds")
# print(f"60 days are {60 * calculations_to_units} {name_of_unit}")
# print(f"44 days are {44 * calculations_to_units} seconds")
# print(f"32 days are {32 * calculations_to_units} {name_of_unit}")

#--------------------------------------------------------------------------------#
def myfunction(num_of_days):
    # print(f"{num_of_days} days are {num_of_days * calculations} {name_of_unit}")
    # print(my_message)

    #conditioncheck= num_of_days>0
    #print(type(conditioncheck))

    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculations} {name_of_unit}"
    elif num_of_days == 0:
        print("You have entered zero , please enter positive number & larger than zero")
    else:
        print("Please enter positive number for the calculation ")


# myfunction(12,"Awesome")
# myfunction(37,"Looks Good")
# myfunction(45,"Great !!!!")

#---------------------------------#
def Scope_check(number):
    var = "This is internal"
    print(calculations)
    print(number)
    print(var)

# Scope_check(10)
# Scope_check(122)
# Scope_check(33)

# valuefromfunction = myfunction(33,"This is the calculation")
# print(valuefromfunction)

print(myfunction(10))