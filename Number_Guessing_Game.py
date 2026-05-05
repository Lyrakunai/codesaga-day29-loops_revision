import random
secret = random.randint(1,50)
attempts = 10
guesses =[] 
won = False
while attempts > 0:
    guess = int(input("guess number between 1 and 50: "))
    if guess == 0:
        print("game exited.")
        break
    if guess in guesses:
        print("you already guessed this number!")
        continue
    attempts -= 1
    guesses.append(guess)
    if guess == secret:
        print("🎉 congratulations! you guessed it right!")
        won = True
        break
    elif guess >= secret - 2 and guess <= secret + 2:
        print("very close!")
    elif guess > secret:
        print("too high")
    else:
        print("too low")
    print("you left",attempts,"attempts ")
if not won and attempts == 0:
    print("game over!")
    print("you used all attempts")
    print("The correct number was:",secret)
