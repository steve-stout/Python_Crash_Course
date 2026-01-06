# This is a rang function to list even numbers 1-10
for value in range(1,5):
    print(value) # this will only print 1-4 (this is the result of the off by one behavior)

even_numbers = list(range(2, 11, 2))
print(even_numbers)