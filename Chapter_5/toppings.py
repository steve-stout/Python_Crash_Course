#checking for inequality
requested_topping = ['pepperoni', 'extra cheese', 'green peppers']

if 'mushroooms' in requested_topping:
    print("Adding Mushrooms.")
if requested_topping == 'green peppers':
    print("Sorry, We are out of green peppers right now.")
else:
    print(f"Adding {requested_topping}.")
if 'pepperoni' in requested_topping:
    print("Adding Pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding Extra Cheese.")    
if requested_topping != 'anchovies':
    print("Hold the Anchovies!")

print("\nFinished making your pizza!")
