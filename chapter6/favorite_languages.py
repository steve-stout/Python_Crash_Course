#Dictionary of similar objects. page 97
favorite_languages ={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

languag = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {languag}")

#for loop page 100
for name, language in favorite_languages.items():
    print(f"{name.title()})'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())

#for loops page 102
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {languag}!")

#WTF page 102
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#page 103
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#page 103 part 2
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#page 104 creating sets
print("The following languages have been mentioned:")
for language in (favorite_languages.values()):
    print(languag.title())