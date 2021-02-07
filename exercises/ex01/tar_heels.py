"""An exercise in remainders and boolean logic."""

__author__ = "730349814"


Num = int(input("Please enter an integer:"))
if Num%2==0 and Num%7!=0:
    print("TAR")
else: 
    if Num%7==0 and Num%2!=0:
        print("HEELS")
    else:
        if Num%2==0 and Num%7==0:
            print("TAR HEELS")
        else: 
            print("CAROLINA")    
