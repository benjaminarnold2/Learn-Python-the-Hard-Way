from random import randint
from sys import exit


def pickpocket():

    print "What are the chances of a successful pick pocket?"

    percentage = raw_input(">")

    percentage = int(percentage)

    pocket = randint(1, 100)

    print pocket

    if percentage < pocket:

        print "Attempt failed!"

    elif percentage >= pocket:

        print "Attempt passed!"

    again = raw_input("Go again?")

    if "y" in again:

        pickpocket()

    else:

        exit()

answer = raw_input("Do you want to pick pocket?")

if "y" in answer:

    pickpocket()

else:

    exit()
