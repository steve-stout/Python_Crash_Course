#maybe this one will work?
available_topping = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_topping:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we dont have {requested_topping}.")

print("\nFinished making your pizza!")