# Guess-The-Number
import random
secret=random.randint(1, 1000)
attempt=0
while True:
    attempt=int(input("Guess the number:"))
    if (secret>attempt):
        print("Too Low")
    elif (secret<attempt):
        print("Too High")
    else:

        break

    

