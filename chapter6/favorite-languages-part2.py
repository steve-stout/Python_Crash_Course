#Favorite languages page 109
favorite_languges = {
    'jen': ['puthon', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],               
}

for name, languages in favorite_languges.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")