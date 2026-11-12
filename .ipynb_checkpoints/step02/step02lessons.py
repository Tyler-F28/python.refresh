# Processing: store values in variables
room = "Room 112"
seats = 24
print(room)
print(seats)

# A variable can be changed later. The old value is replaced.
seats = 30
print(seats)
count = 5
count = count + 1    # take the old count (5), add 1, store 6 back in count
print(count)
# Processing: check the type of some values
print(type("Jordan"))
print(type(3))
print(type(2.75))
print(type(True))
print(type("3"))
print('Tyler F')
print(12)
print(2.9)
print(type('Tyler F'))
print(type(12))
print(type(2.9))
# Input: ask for the user's first name
first_name = input("First name: ")

# Output: greet them
print("Hello, " + first_name + "!")
# Input: read the age as text, then convert it to a whole number
age_text = input("Age: ")
age = int(age_text)

# Processing: math only works on numbers
age_next_year = age + 1

# Output
print("Next year you will be", age_next_year)
# Processing: some math examples
minutes = 135
hours = minutes // 60          # whole hours
leftover = minutes % 60        # minutes left over
print(hours, "hours and", leftover, "minutes")

average = (80 + 90 + 85) / 3   # parentheses: add first, then divide
print(average)

wrong_average = 80 + 90 + 85 / 3   # divides only the 85!
print(wrong_average)
# Processing: int() chops, round() rounds
price = 8.99
print(int(price))
print(round(price))
print(round(8.8275, 2))
# Named constants (ALL_CAPS means "do not change this")
SALES_TAX_RATE = 0.0675
SHIPPING_COST = 4.99

# Processing: use the names instead of typing the numbers again
order_amount = 40.00
tax = order_amount * SALES_TAX_RATE
total = order_amount + tax + SHIPPING_COST
print(f"Total: ${total:.2f}")    # :.2f is explained in the next section
# Processing: some values to show
player = "Casey"
points = 42
cost = 3.5

# Output: f-strings put values right into the text
print(f"{player} scored {points} points.")
print(f"Cost: ${cost}")
print(f"Cost: ${cost:.2f}")
# Name: Your Name
# Date: 2026-11-06
# Program: Carpet Cost Example
# Description: Works out the cost to carpet a room, plus a fee.

# Named constant for the install fee
INSTALL_FEE = 25.00

# Input: room owner, cost per square foot, and room size
owner = input("Owner: ")
cost_per_foot = float(input("Cost per square foot: "))
square_feet = int(input("Square feet: "))

# Processing: material cost and total
material_cost = cost_per_foot * square_feet
total_cost = material_cost + INSTALL_FEE

# Output: a small report, money to 2 decimal places
print()
print(f"--- Estimate for {owner} ---")
print(f"Material:  ${material_cost:.2f}")
print(f"Install:   ${INSTALL_FEE:.2f}")
print(f"Total:     ${total_cost:.2f}")
