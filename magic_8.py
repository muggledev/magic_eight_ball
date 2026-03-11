import random


rand_num = random.randrange(1,9)


question = input("\nAsk me a question and I will predict the outcome.\n(press enter to quit)\n")

if rand_num == 1:
    print("I like the idea")
elif rand_num == 2:
    print("These are not the droids you are looking for")
elif rand_num == 3:
    print("Difficult. Very Difficult......I think yes")
elif rand_num == 4:
    print("What?!")
elif rand_num == 5:
    print("I guess so")
elif rand_num == 6:
    print("It will never be so")
elif rand_num == 7:
    print("Come back tomorrow and I will then have your answer")
elif rand_num == 8:
    print("I think I hear the hallelujah chorus")