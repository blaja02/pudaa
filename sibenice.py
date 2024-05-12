word = input("enter your word for the game:")
position_in_word = 0
what_you_guessed = ""
for position_in_word, char in enumerate(word):
    guess= input("enter your letter guess:") 
    for char in word:
        if guess==char:
            print("you guessed right!")
            what_you_guessed += guess
            break
        else:
            print ("you didn't guess", position_in_word , "right")

#    print("position in word is:")
