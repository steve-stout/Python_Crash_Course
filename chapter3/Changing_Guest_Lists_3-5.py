# Invite some people to dinner
guests = ['guido vabn russum', 'jack turner', 'lynn hill']

name = guests[0].title()
print(f"{name}, please come to dinner")

name = guests[1].title()
print(f"{name}, please come to dinner")

name = guests[2].title()
print(f"{name}, please come to dinner")

name = guests[1].title()
print(f"\nSorry, {name} cant make it to dinner.")

# Jack cant make it, he died. Lets invite Gary because he is still alive.
del(guests[1])
guests.insert(1, 'gary snyder')

#Print the invitations again.
name = guests[0].title()
print(f"\n{name}, Please come to dinner.")

name = guests[1].title()
print(f"\n{name}, Please come to dinner.")

name = guests[2].title()
print(f"\n{name}, Please come to dinner.")