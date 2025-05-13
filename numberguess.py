import random

user_guess = int(input("GUESS A Number from 1 To 10:\n"))

py_guess = random.randint(1,10)
print("Python Has GUESSED :",py_guess)

if user_guess != py_guess:
    print("YOU HAVE GUESSED WRONG 🔪🔪🔪")
else:
    print("YES YOU HAVE GUESSED RIGHT🍾🍾🍾🥳")