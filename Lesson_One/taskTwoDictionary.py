
#List of Dictionary not Dictionary itself practice
people = [
    {"name": "Chris", "age": 40},
    {"name": "Alex", "age": 25},
    {"name": "Jordan", "age": 35},
    {"name": "Mike", "age": 41}
]

#the first part is what you end up displaying, if you want in include age then
#  peoples["name"]: peoples["age"]
olderThanThirty = {peoples["name"] for peoples in people if peoples["age"] > 30}

print((olderThanThirty))