# This is a rang function to print square numbers
for value in range(1,5):
    print(value) # this will only print 1-4 (this is the result of the off by one behavior)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2 #** us the integer 2 is the square (3 would be cubed).
    squares.append(square)

print(squares)

> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45