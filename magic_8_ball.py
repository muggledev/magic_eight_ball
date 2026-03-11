import random


rand_num = random.randrange(1,9)

# Code goes here:

# Input for their question

# Conditionals to display the answers based on that random number.


question = input("Ask me a question and I will predict the outcome.")


if rand_num == 1:
    print("Reply Hazy, Try Again")
elif rand_num == 2:
    print("Cannot Predict Now")
elif rand_num == 3: 
    print("Signs point to YES!")
elif rand_num == 4:
    print("I plead the 5th!")
elif rand_num == 5:
    print("Ha! Another Weasley! I know just what to tell you.......No")
elif rand_num == 6:
    print("Plan on it!")
elif rand_num == 7:
    print("It's likely")
elif rand_num == 8:
    print("These are not the droids you are looking for")