import random
name = input("Hello! What is your name?") 
print(f"""Well {name}, I am thinking of a number between 1 and 20.
Take a guess.""")
num = random.randint(1,20)
counter = 0


while True:
    guess = int(input())
    counter +=1
    if (guess == num):
        print(f"Good job, KBTU! You guessed my number in {counter} guesses!")
        break
    elif (guess > num):
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
