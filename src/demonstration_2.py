"""
You are a new author that is working on your first book. You are working on a
series of drafts. Each draft is based on the previous draft. The latest draft
of your book has a serious typo. Since each newer draft is based on the
previous draft, all the drafts after the draft containing the typo also include
the typo.

Suppose you have `n` drafts `[1, 2, 3, ..., n]` and you need to find out the
first one containing the typo (which causes all the following drafts to have
the typo as well).

You are given access to an API tool `containsTypo(draft)` that will return
`True` if the draft contains a typo and `False` if it does not.

You need to implement a function that will find the *first draft that contains
a typo*. Also, you have to pay a fee for every call to `containsTypo()`, so
make sure that your solution minimizes the number of API calls.

Example:

Given `n = 5`, and `draft = 4` is the first draft containing a typo. <--- Five drafts and draft num 4 has the og typo

containsTypo(3) -> False
containsTypo(5) -> True
containsTypo(4) -> True
"""
#
def containsTypo(n):
    if n >= 4:
        return True
    else:
        return False

def firstDraftWithTypo(n):
    floor = 1
    ceiling = n

    while floor < ceiling:
        guess = ((ceiling - floor) // 2) + floor
        print(f'guess: {guess}')

        if guess == ceiling:
            return floor
        elif guess == floor:
            return ceiling


        # Move floor and ceiling accordingly
        if containsTypo(guess):
            ceiling = guess
        else:
            floor = guess

print(firstDraftWithTypo(100000))
