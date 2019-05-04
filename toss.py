import random as R
def toss():
    a = input ("Enter 0 for Heads and 1 for Tails : ")
    b = R.choice( [ 0, 1 ] )
    if ( a == b):
        return 0
    else :
        return 1

def result():
    c = toss()
    if ( c == 0 ):
        print ( "You Won The Toss " )
    else :
        print ( "You Lost The Toss " )
result()
