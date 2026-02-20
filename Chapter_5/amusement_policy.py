#if-elif-else
age = 12
if age < 4:
    print("Your admission is free.")
elif age < 18:
    print("your admission cost is $25")
else:
    print("Your admission cost is $40")

#Part 2 this is easier to modify than the previous.
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 100

print(f"Your addmission cost is ${price}.")

#Part 3 using multiple elif statments. pay attention to the < >.
age = 67

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age > 65:
    price = 500
else:
    price = 20

print(f"Your addmission cost is ${price}.")

#Part 4 you dont need an else statement
age = 25

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age > 65:
    price = 500


print(f"Your addmission cost is ${price}.")