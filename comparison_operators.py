"""
Task 1 - comparison operators
Your task is to write a program which asks the user 
three times about two integer numbers to compare.
"""

# Num1 = int(input("Enter first number: "))
# Num2 = int(input("Enter second number: "))

# if Num1 != Num2:
#     print("The Numbers are not equal.")
# if Num1 > Num2: 
#     print("The first Number is greater than the second")
# elif Num1 < Num2:
#     print("The second Number is greater than the first")
# if Num1 <= Num2:
#     print('The second Number is greater than or equal to the first')
# bignumbers = False
# if Num1 != bignumbers and Num2 != bignumbers:
#     print('The both Numbers are not big!')


"""
Task 2 - convertion month name to a number of days
Your task is to write a Python program to convert month name to a number of days.
"""

month_name = input("Enter the name of Month : ")

ListOfMonths = ["January", "February", "March", "April", "May", 
                    "June", "July", "August", "September", "October", 
                    "November", "December"]

if month_name == ListOfMonths[0]:
    print(ListOfMonths[0], "has 31 days. ")
elif month_name == ListOfMonths[1]:
    print( ListOfMonths[1], "has 28 days. ")
elif month_name == ListOfMonths[2]:
    print( ListOfMonths[2], "has 31 days. ")
elif month_name == ListOfMonths[3]:
    print( ListOfMonths[3], "has 30 days. ")
elif month_name == ListOfMonths[4]:
    print(ListOfMonths[4], "has 31 days. ")
elif month_name == ListOfMonths[5]:
    print( ListOfMonths[5], "has 30 days. ")
elif month_name == ListOfMonths[6]:
    print( ListOfMonths[6], "has 31 days. ")
elif month_name == ListOfMonths[7]:
    print(ListOfMonths[7], "has 31 days. ")
elif month_name == ListOfMonths[8]:
    print(ListOfMonths[8], "has 30 days. ")
elif month_name == ListOfMonths[9]:
    print(ListOfMonths[9], "has 31 days. ")
elif month_name == ListOfMonths[10]:
    print(ListOfMonths[10], "has 30 days. ")
elif month_name == ListOfMonths[11]:
    print(ListOfMonths[11], "has 31 days. ")
