"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730349814"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint
print("Your fortune cookie says...")
Cookie = randint(1,4)
if Cookie == 1:
    print("No snowflake in an avalanche ever feels responsible")
else:
    if Cookie == 2:
        print("You have a secret admirer")
    else:
        if Cookie == 3:
            print("A faithful friend is a strong defense")
        else:
            print("When one door closes, another opens")     
print("Now, go spread positive vibes!")