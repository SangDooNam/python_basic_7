"""
Task 1 - comparison operators
Your task is to write a program which asks the user 
three times about two integer numbers to compare.
"""

# count = 0
# big_numbers = True

# while count < 3:

#     Num1 = int(input("Enter first number: "))
#     Num2 = int(input("Enter second number: "))

#     if Num1 != Num2:
#         print("The numbers are not equal.")
#     else:
#         print('The numbers are equal')
#     if Num1 > Num2: 
#         print("The first number is greater than the second")
#     elif Num1 < Num2:
#         print("The second number is greater than the first")
#     if Num1 <= Num2:
#         print('The second number is greater than or equal to the first')
#     elif Num1 >= Num2:
#         print('The scond number is less than or equal to the first')
    
#     if Num1 > 1000 and Num2 > 1000:
#         big_numbers = True
#         print('Both numbers are big !')
#     else:
#         big_numbers = False
#         print('Both numbers are not big!')
        
#     print('big_numbers is set to', big_numbers )
    
#     count += 1


    
    

"""
Task 2 - convertion month name to a number of days
Your task is to write a Python program to convert month name to a number of days.
"""

# month_name = input("Enter the name of Month : ")

# ListOfMonths = ["January", "February", "March", "April", "May", 
#                     "June", "July", "August", "September", "October", 
#                     "November", "December"]

# if month_name == ListOfMonths[0]:
#     print(ListOfMonths[0], "has 31 days. ")
# elif month_name == ListOfMonths[1]:
#     print( ListOfMonths[1], "has 28 days. ")
# elif month_name == ListOfMonths[2]:
#     print( ListOfMonths[2], "has 31 days. ")
# elif month_name == ListOfMonths[3]:
#     print( ListOfMonths[3], "has 30 days. ")
# elif month_name == ListOfMonths[4]:
#     print(ListOfMonths[4], "has 31 days. ")
# elif month_name == ListOfMonths[5]:
#     print( ListOfMonths[5], "has 30 days. ")
# elif month_name == ListOfMonths[6]:
#     print( ListOfMonths[6], "has 31 days. ")
# elif month_name == ListOfMonths[7]:
#     print(ListOfMonths[7], "has 31 days. ")
# elif month_name == ListOfMonths[8]:
#     print(ListOfMonths[8], "has 30 days. ")
# elif month_name == ListOfMonths[9]:
#     print(ListOfMonths[9], "has 31 days. ")
# elif month_name == ListOfMonths[10]:
#     print(ListOfMonths[10], "has 30 days. ")
# elif month_name == ListOfMonths[11]:
#     print(ListOfMonths[11], "has 31 days. ")


print('List of months: January, February, March, April, May, June, July, August, September, October, November, December')



name_of_Month = input('The name of Month: ')

while True:
    
    if name_of_Month in ('january','January', 'march', 'March', 'may', 'May', 'july', 'July', 'August', 'august', 'October', 'october', 'December', 'december' ):
        print(name_of_Month, "has 31 days. ")
        break
    elif name_of_Month in ('april', 'April', 'june', 'June', 'september', 'September', 'november', 'November'):
        print(name_of_Month, "has 30 days. ")
        break
    elif name_of_Month in ('february', 'February'):
        print(name_of_Month, "has 28 days. ")
        break
    else:
        name_of_Month = input('Enter the valid name of Month: ')

        