"""
I was bored one day and decided to look at last names in the phonebook for my
area.

I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.

When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."

Example:

surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]

Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.

*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""
names = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]

names2 = [
    'frankie',
    'geegee',
    'Harley',
    'ava',
    'becca',
    'charlie',
]

def find_rotation_point(surnames):
    floor = 0
    ceiling = len(surnames) - 1
    first_name = surnames[0]

    while floor < ceiling:
        guessIndex = ((ceiling - floor) // 2) + floor
        guess = surnames[guessIndex]
        prevName = surnames[guessIndex - 1]

        if prevName > guess:
            return guessIndex

        if guess < first_name:
            ceiling = guessIndex

        if guess > first_name:
            floor = guessIndex



print(find_rotation_point(names))
print(find_rotation_point(names2))
