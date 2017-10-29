


guess = 50
print("Please think of a number between 0 and 100!")
while True:
    print ("Is your secret number "+str(int(guess))+"?")
    val = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if val == "h":
        guess = guess - (100-guess)/2
    elif val == "l":
        guess = guess + (100-guess) /2
    elif val == "c":
        print ("Game over. Your secret number was: "+str(int(guess)))
        break
    else:
        print("Sorry, I did not understand your input.")
        continue
