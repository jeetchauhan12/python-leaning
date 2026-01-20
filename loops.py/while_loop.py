
import random
sum = random.randint(1,100)
print(sum)

while True :
    guess = int(input("any alphbat u put in the frame:-"))

    tries = 0

    if sum == guess:
        print(f"you guess {tries} the correct one")
        tries += 1 
        break

    elif sum < guess:
        print ("you have to go little lower ")
        tries += 1

    elif sum > guess:
        print ("you have to go little higher ")
        tries += 1

    else:
        print(f" you guess in the answer in {tries} after this many time")
        tries += 1