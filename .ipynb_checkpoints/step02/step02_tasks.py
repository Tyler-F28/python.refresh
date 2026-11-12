SLICES_PER_PIZZA = 8
PIZZA_PRICE = 12.99
SLICE_PRICE = 2.25
people = 10
slices_per_person = 3
total_slices = slices_per_person * people
whole_pizzas = total_slices // SLICES_PER_PIZZA
extra_slices = total_slices % SLICES_PER_PIZZA
total_cost = whole_pizzas * PIZZA_PRICE + extra_slices * SLICE_PRICE
cost_per_person = total_cost / people
print('Host name: Jordan \nNumber of people: 10')
print('Slices per person: 3')
print('')
print('=== Pizza Plan for Jordan\'s Party ===')
print(f'Slices needed: {total_slices}')
print(f'Whole pizzas: {whole_pizzas}')
print(f'Extra slices: {extra_slices}')
print(f'Total cost: ${total_cost:.2f}')
print(f'Cost per person: ${cost_per_person:.2f}')
print('')
DISTANCE = 150
MILES_PER_GALLON = 30
GAS_PRICE =3.20
PEOPLE = 2
AVERAGE_SPEED = 55
destination = 'Columbus'
gallons = DISTANCE / MILES_PER_GALLON
gas_cost = gallons * GAS_PRICE
cost_per_person = gas_cost / PEOPLE
driving_time = int(DISTANCE / AVERAGE_SPEED * 60) # Converts the total minutes to an integer
hours = driving_time // 60
leftover_minutes = driving_time % 60
round_trip_cost = gas_cost * 2
int(leftover_minutes)
print(f'Destination: {destination}')
print(f'Trip distance (miles): {DISTANCE}')
print(f'Car\'s miles per gallon: {MILES_PER_GALLON}')
print(f'Gas price per gallon: ${GAS_PRICE:.2f}')
print(f'Number of people splitting the cost: {PEOPLE}')
print('')
print('--- Trip to Columbus ---')
print(f'Gallons of gas:   {gallons:.1f}')
print(f'Gas cost:         ${gas_cost:.2f}')
print(f'Cost per person:  ${cost_per_person:.2f}')
print(f'Driving time:     {hours, leftover_minutes}')
print(f'Round trip gas:   ${round_trip_cost:.2f}')
print('')
FEDERAL_TAX_RATE = 0.10
STATE_TAX_RATE = 0.035
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145
WEEKS_PER_YEAR = 52
rate = 16.00
hours = 25
gross_pay = rate * hours
state = STATE_TAX_RATE * gross_pay
federal = FEDERAL_TAX_RATE * gross_pay
social = SOCIAL_SECURITY_RATE * gross_pay
medicare = MEDICARE_RATE * gross_pay
total_taken = state + federal + social + medicare
net_pay = gross_pay - total_taken
percent_kept = net_pay / gross_pay *100
yearly_gross = gross_pay * WEEKS_PER_YEAR
yearly_net = net_pay * WEEKS_PER_YEAR
print('Employee name: Avery')
print(f'Hourly pay rate: {rate}')
print(f'Hours worked this week: {hours}')
