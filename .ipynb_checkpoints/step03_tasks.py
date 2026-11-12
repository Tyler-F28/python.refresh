CHILD_PRICE = 7.00 
ADULT_PRICE = 11.00 
SENIOR_PRICE = 8.00 
TUESDAY_DISCOUNT = 3.00 
THREE_D_CHARGE = 2.50 

name = input("what's your name: ")
age = int(input("what's your age: "))
day = input("which day will you see it: ").strip().lower()
threed = input("will it be 3d: y/n: ").strip().lower()

print(f'\nName: {name}')
print(f'Age: {age}')
print(f'Day of the week: {day}')
print(f'3D movie? (y/n): {threed}\n')
print(f'--- Ticket for {name} ---')
if age < 0 or age > 120:
    print('Error: age must be 0 to 120.')
    base_price = 0
elif age >= 65:
    print('Ticket type: Senior')
    print(f'Base price: ${SENIOR_PRICE:.2f}')
    base_price = SENIOR_PRICE
elif age < 13:
    print('Ticket type: Child')
    print(f'Base price: ${CHILD_PRICE:.2f}')
    base_price = CHILD_PRICE
else:
    print('Ticket type: Adult')
    print(f'Base price: ${ADULT_PRICE:.2f}')
    base_price = ADULT_PRICE

# Apply Tuesday discount directly to the base price
if day == 'tuesday':
    base_price -= TUESDAY_DISCOUNT
    print(f'Tuesday deal: -${TUESDAY_DISCOUNT:.2f}')

# Apply 3D charge directly to the base price
if threed == 'y':
    print(f'3D charge: ${THREE_D_CHARGE:.2f}')
    base_price += THREE_D_CHARGE
elif threed != 'n':
    print('Error: y/n only valid response')

print(f'Total Price: ${base_price:.2f}')
print('')
print('')
print('')
# Constants for shipping rates and thresholds
ZONE1_RATE = 0.50
ZONE2_RATE = 0.75
ZONE3_RATE = 1.25
MINIMUM_SHIPPING = 4.00
FREE_SHIPPING_AMOUNT = 50.00
RUSH_FEE = 10.00

# --- Input Section ---
# Ask for user inputs using the required data types
order_total = float(input("Enter order total: "))
weight = float(input("Enter package weight in pounds: "))
zone = int(input("Enter shipping zone: "))
rush_delivery = input("Rush delivery (y/n)? ").lower()

# --- Validation Section ---
# Validate order total and weight
if order_total <= 0 or weight <= 0:
    print("Error: order total and weight must be more than 0.")
# Validate the shipping zone (Ensuring it is strictly 1, 2, or 3)
elif zone not in(1, 2, 3):
    print("Error: zone must be 1, 2, or 3.")
else:
    # --- Processing Section ---
    # 1. Calculate base shipping rate and base delivery days
    if zone == 1:
        shipping = weight * ZONE1_RATE
        days = 2
    elif zone == 2:
        shipping = weight * ZONE2_RATE
        days = 4
    else:  # zone == 3
        shipping = weight * ZONE3_RATE
        days = 6

    # 2. Apply minimum shipping fee rule
    if shipping < MINIMUM_SHIPPING:
        shipping = MINIMUM_SHIPPING

    # 3. Apply free shipping rule (if total qualifies and it's NOT rush)
    if order_total >= FREE_SHIPPING_AMOUNT and rush_delivery != 'y':
        shipping = 0.0

    # 4. Apply rush delivery adjustments
    if rush_delivery == 'y':
        shipping += RUSH_FEE
        # If zone is 1 or 2, rush takes 1 day
        if zone in(1,2):
            days = 1
        else:  # zone == 3
            days = 2

    # 5. Apply heavy package rule
    if weight > 50:
        days += 2

    # --- Output Section ---
    print(f'Order total: ${order_total:.2f}')
    print(f'Package weight (lbs): {weight}')
    print(f'Shipping zone (1-3): {zone}')
    print(f'Rush delivery? (y/n): {rush_delivery}')
    print('')
    print("\n--- Shipping Summary ---")
    # Format shipping cost: display "FREE" if 0, otherwise format as currency
    if shipping == 0:
        print("Shipping Cost: FREE")
    else:
        print(f"Shipping Cost: ${shipping:.2f}")

    # Format days: handle singular "day" vs plural "days"
    if days == 1:
        print("Delivery Time: 1 day")
    else:
        print(f"Delivery Time: {days} days")

    # Print the heavy package note if applicable
    if weight > 50:
        print("Note: Package is heavy. Additional transit days have been applied.")
print('')
print('')
print('')
# Program: BPA Member Eligibility Checker
# Description: Checks member eligibility, event counts, and leadership/honor status.

# Constants
MIN_GPA = 2.0
OFFICER_GPA = 3.0
HONOR_GPA = 3.5
MAX_EVENTS = 2

# Input
member_name = input("what's your name:")
grade = int(input("what's your grade (9-12):"))
gpa = float(input("what's your GPA:"))
dues = input("are your dues paid (y/n):")
events = int(input("how many events (max 2):"))

# Processing & Output
if grade < 9 or grade > 12:
    print("Error: grade must be 9 to 12.")
elif gpa < 0.0 or gpa > 4.0:
    print("Error: GPA must be 0.0 to 4.0.")
else:
    print(f"--- BPA Check for {member_name} ---")
    
    # Check eligibility using named constants
    if gpa >= MIN_GPA and dues.lower() == 'y':
        print("Status: ELIGIBLE")
        
        if events <= 0:
            print("Sign up for at least one event.")
        elif events == 1:
            print("You are entered in 1 event.")
        elif events == 2:
            print("You are entered in 2 events.")
        else:
            extra_events = events - MAX_EVENTS
            print(f"You can only enter 2 events. Drop {extra_events}.")
    else:
        print("Status: NOT ELIGIBLE")
        
        if dues.lower() != 'y':
            print("Reason: dues not paid.")
        if gpa < MIN_GPA:
            print("Reason: GPA is below 2.0.")

    # Check officer and honor cord status for anyone who passed input validation
    if (grade == 11 or grade == 12) and gpa >= OFFICER_GPA:
        print("You can run for chapter office.")
        
    if grade == 12 and gpa >= HONOR_GPA:
        print("Senior honor cord: yes")
