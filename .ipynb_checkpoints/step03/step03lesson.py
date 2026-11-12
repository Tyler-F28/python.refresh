# Processing: comparisons give back True or False
score = 75
print(score >= 60)
print(score == 100)

passed = score >= 60      # you can store the answer in a variable
print(passed)
# The program already knows how many are left
tickets_left = 4

# Input: how many tickets the user wants
wanted = int(input("How many tickets? "))

# Processing and Output: warn only when there aren't enough
if wanted > tickets_left:
    print("Sorry, only", tickets_left, "tickets are left.")
    print("Please choose a smaller number.")
print("Thanks for checking.")
# Input
age = int(input("Age: "))

# Processing and Output: one of two messages
if age >= 16:
    print("You can sign up for the driving class.")
else:
    years_left = 16 - age
    print(f"You can sign up in {years_left} year(s).")
# Input
temperature = int(input("Temperature: "))

# Processing: pick one description, checking from the top down
if temperature >= 90:
    description = "hot"
elif temperature >= 70:
    description = "warm"
elif temperature >= 50:
    description = "cool"
else:
    description = "cold"

# Output
print(f"It is {description} today.")
# Input
rating = int(input("Rating (1-5): "))

# Processing and Output: "or" because it is bad if EITHER side is true
if rating < 1 or rating > 5:
    print("Error: rating must be 1 to 5.")
else:
    print(f"Thanks for rating us {rating} out of 5.")# Input
rating = int(input("Rating (1-5): "))

# Input
age = int(input("Age: "))
member = input("Club member? (y/n): ")

# Processing and Output: the inner check only happens for adults
if age >= 18:
    if member == "y":
        print("Ticket price: $6.00")
    else:
        print("Ticket price: $9.00")
else:
    print("Ticket price: $4.00")
answer = "Yes"
print(answer == "yes")          # capital Y vs small y
print(answer.lower() == "yes")  # .lower() makes a lowercase copy first
print(answer.upper())           # .upper() makes an uppercase copy
choice = "Y"
# Way 1: check both with "or"
if choice == "y" or choice == "Y":
    print("Way 1: yes")
# Way 2: lowercase it first, then check once
if choice.lower() == "y":
    print("Way 2: yes")
choice = 2
# Processing: match picks the case that equals choice
match choice:
    case 1:
        print("Add member")
    case 2:
        print("Record points")
    case _:
        print("Unknown option")   # _ means "anything else"
