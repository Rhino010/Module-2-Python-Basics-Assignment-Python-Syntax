# Task 1: Grocery Store Math
# Declaring the initial prices for the bread, peanut butter, and the jelly.
bread = 5.19
peanut_butter = 6.44
jelly = 3.27

# Setting a variable 'total' to the sum of the items
total = bread + peanut_butter + jelly
print(f'Your total for the bread, peanut butter, and jelly is... ${total}')

# Using a tax of 10% and multiplying the total by 1.1 to get the total with tax.
tax = .1
total_w_tax = total * (1 + tax)
print(f"Don't forget about Uncle Sam. Your total with tax is... ${total_w_tax}")


# Task 2: Bank Interest
# Allowing the user to declare the variables and added the int() method to convert the input string to an integer
savings = int(input("How much money do you have in your savings?\n$"))
interest_rate = int(input("What percent is your bank's interest rate?\n%"))

# declaring total_w_interest as the value of the original savings plus the interest of that savings amount
total_w_interest = savings + savings * (interest_rate / 100)
print(f"After one year your total with interest will be ${total_w_interest}")