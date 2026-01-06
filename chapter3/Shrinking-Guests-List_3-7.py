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

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table! So the Beheadings can begin immediately")
guests.insert(0, 'frida kalo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")

#Fuck, the table got held up in customes.
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)