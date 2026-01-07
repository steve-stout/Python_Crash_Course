#This is how to copy a list in python
my_foods = ['pizza', 'spaghetti', 'tacos', 'chicken', 'salad', 'steak', 'fries']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
