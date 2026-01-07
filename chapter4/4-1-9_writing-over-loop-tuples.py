#Python refers to values that cannot change as immutable, and an immutable list is called a tuple
dimensions = (200, 50)
print ("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

