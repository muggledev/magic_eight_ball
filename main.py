# Booleans

    # computers are very simple minded. They think in 1's and 0's.
    # Boolean Values are:
        # Ture or False
    # We see True or False
    # the computer sees 1 or 0

    # Boolean opperators
        # AND
        # OR
        # NOT
        # XOR

    # Boolean Expressions
        # A Boolean expression is similar to a math expression
        # the difference between a math expression and a boolean expression is that math gets to use all numbers when boolean uses True and False.


    # examples:
        # True == False
        # True == True AND False == False
        # False OR True AND False


# The opperator AND will allow for two boolean values to be compared.
    # If one of the compared boolean values is False than the result will come out False.
    # If both boolean values are True the result will come out True.



    # AND Truth Table
    #       True	False
    # True	True	False
    # False	False	False


# The operator OR will compare two boolean values.
    # if you have one boolean value that is True the result will come out True.

# OR
#         True     False
#       -----------------
# True  |  True  |  True
#       |----------------
# False |  True  |  False



# The operator NOT will help the Boolean value change its identity.
    # The NOT operator toggles the boolean value to be the opposite value.

# NOT Truth Table

#     True	False
#     False	True



# XOR Truth Table

#       True	False
# True	False	True
# False	True	False



# We solve this just like math, start with the parentheses and going left to right, using the charts.
# False OR (True AND NOT(False OR True))
# False OR (True AND NOT Ture)
# False OR (True AND False)
# False OR False
# False


# True AND False OR True = True

# False OR True AND NOT False = True

# True OR (False OR True) AND False = True

# NOT(True OR False) AND NOT(True XOR True) = False

# True OR False AND True OR False = True

# True AND (False AND (True OR False)) = False





# new_number = input("Enter a new number here: ")

# new_int = int(new_number)

# if new_int > 100:
#     print("Your number is too big.")

# elif new_int < 80:
#     print("Your number is too small.")

# else:
#     print("Your number is perfect.")








# user_name = "John"
# email = "john_wick@gmail.com"
# password = "I'mBack"

# if (user_name == "John" or email == "john_wick@gmail.com") and password == "I'mBack":
#     print("Welcome duder!")
# else:
#     print("No business on Continental grounds!")




# grade = 75

# if grade < 60:
#     print("F")
# elif grade < 60:
#     print("D")
# elif grade > 70:
#     print("C")
# elif grade > 80:
#     print("B")
# elif grade > 90:
#     print("A")
# else:
#     print("I hope this works")


grade_int = 89


if grade_int == 100:
    print('A')
elif grade_int > 90:
    print('A')
elif grade_int > 80:
    print('B')
elif grade_int > 70:
    print('C')
elif grade_int > 60:
    print('D')
elif grade_int < 60:
    print('F')
else:
    print("Needs more work")