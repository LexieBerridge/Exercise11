wordoftheday = "hello"  # to change the word in the game this is the only valuable you would need to edit
hintmax = 3
hintattempts = 1
hint1 = wordoftheday[0]
hint2 = wordoftheday[1]
hint3 = wordoftheday[2]
numberofattempts = 5
attempt = 1
wordofthedaystring = [i for ele in wordoftheday for i in ele]

print("Word of the Day =", ("_" * len(wordoftheday)))
while attempt < numberofattempts:
    guess = input("Please enter your answer:")
    guessstring = [i for ele in guess for i in ele]
    if len(guess) == len(wordoftheday):
        if wordoftheday == guess:
            print("Got it, the word is ", wordoftheday)
            break
        elif guess != wordoftheday:
            if any(item in wordofthedaystring for item in guessstring):
                print("Close, you got some letters there", "attempt", attempt, "/", numberofattempts)
                attempt = attempt + 1
                answer = input("would you like a clue Y/N")
                y = "y"
                Y = "Y"
                if answer == y or answer == Y:
                    if hintattempts == 1:
                        print(hint1, ("_" * (len(wordoftheday) - 1)))
                        hintattempts = hintattempts + 1
                    elif hintattempts == 2:
                        print(hint1, hint2, ("_" * (len(wordoftheday) - 2)))
                        hintattempts = hintattempts + 1
                    elif hintattempts == 3:
                        print(hint1, hint2, hint3, ("_" * (len(wordoftheday) - 3)))
                        hintattempts = hintattempts + 1
                    else:
                        print("Ooops you're all out of hints")
                        pass
                else:
                    pass
            else:
                print("nope lol try again", "attempt", attempt, "/", numberofattempts)
                attempt = attempt + 1
                answer = input("would you like a clue Y/N")
                y = "y"
                Y = "Y"
                if answer == y or answer == Y:
                    if hintattempts == 1:
                        print(hint1, ("_" * (len(wordoftheday) - 1)))
                        hintattempts = hintattempts + 1
                    elif hintattempts == 2:
                        print(hint1, hint2, ("_" * (len(wordoftheday) - 2)))
                        hintattempts = hintattempts + 1
                    elif hintattempts == 3:
                        print(hint1, hint2, hint3, ("_" * (len(wordoftheday) - 3)))
                        hintattempts = hintattempts + 1
                    else:
                        print("Ooops you're all out of hints")
                        pass
                else:
                    pass
        else:
            pass
    else:
        print("5 letters you moron", "attempt", attempt, "/", numberofattempts)
        attempt = attempt + 1
        answer = input("would you like a clue Y/N")
        y = "y"
        Y = "Y"
        if answer == y or answer == Y:
            if hintattempts == 1:
                print(hint1, ("_" * (len(wordoftheday) - 1)))
                hintattempts = hintattempts + 1
            elif hintattempts == 2:
                print(hint1, hint2, ("_" * (len(wordoftheday) - 2)))
                hintattempts = hintattempts + 1
            elif hintattempts == 3:
                print(hint1, hint2, hint3, ("_" * (len(wordoftheday) - 3)))
                hintattempts = hintattempts + 1
            else:
                print("Ooops you're all out of hints")
                pass
        else:
            pass
else:
    print("You're all out of attempts")
