import sys
import random


ans = True

while ans:
    question = input("Ask the fuckin question dog: (press enter to quit) ")

    answers = random.randint(1,8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print("Fo sho")

    elif answers == 2:
        print("Ah hell yeah")

    elif answers == 3:
        print("Prolly")

    elif answers == 4:
        print("I'm tired of dis")

    elif answers == 5:
        print("Correct yoself")

    elif answers == 6:
        print("I don't know yo")

    elif answers == 7:
        print("Hell nah")

    elif answers == 8:
        print("Prolly not")
