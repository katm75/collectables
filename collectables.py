# Kathryn Marks
# kathryn.pythonprograms@gmail.com
# Created September 22, 2023
# Last modified November 4, 2023

# Excerise 5 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md
#     Modified to change cryptocurrency to collectables

# You are interested in buying collectables. 
# You want to check the current amount of money you have and see how many things you can buy in the categories of 
# dolls, books or stamps.

# Create a program that:
    # Reads the total amount of money you have
    # Reads the price of dolls, books and stamps
    # Prints the amount of dolls, books and stamps you can buy
    # Example: money = 100, doll_price = 50, book_price = 25, stamp_price = 10
    # Output: "With 100$ you can buy: 2 dolls, 4 book, or 10 stampss"

# BEGIN PROGRAM

# DEFINE VARIABLES
    # money = the amount of money you have to spend in dollars
    # doll_price = the price of dolls
    # book_price = the price of books
    # stamp_price = the price of stamps
    # dolls = number of dolls that can be bought
    # books = number of books that can be bought
    # stamps = number of stamps that can be bought
    
# GET USER INPUT

money = float(input("Please type in the amount of money you have to spend: ")) 
doll_price = float(input("Please type in the cost of dolls: ")) 
book_price = float(input("Please type in the cost of books: ")) 
stamp_price = float(input("Please type in the cost of stamps: ")) 

# CALCULATION GO HERE

# use integer division (//) to get the number of items you can by using a set amount of money.  
# you can't have fractional objects
# but you will get a float if the inputs are floats
# so use regular division inside the int function

dolls = int(money / doll_price)
books = int(money // book_price)
stamps = int(money // stamp_price)

 

# PRINT THE OUTPUT

print("With " + str(money) + " dollars you can buy " + str(dolls) + " dolls or " + str(books) + " books or " + str(stamps) + " stamps")

# #EOF