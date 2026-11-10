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
