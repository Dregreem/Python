import random

cards=["jack","queen","king"]

def main():
    # K amount cards are chosen with from list, a variavle can be chosen twice+
    #print(random.choices(cards,k=2))

    #Again from K amount of cards but this time an item cant be used twice
    #print(random.sample(cards,k=2))

    #weights shows the probability of the variable- the sum must be 100
    #print(random.choices(cards,weights=[70,15,10],k=2))

    # the seed is like the address of the randomness 
    # therefore if we set the seed it will give the same result
    random.seed(0)
    print(random.choices(cards,k=2))



main()