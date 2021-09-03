#Making a word guesser game where the user has to guess the word I'm storing(with the total number of attempts.)I don't know how to use high scores yet so maybe later
#In this version, there's an option to replay it after the user guessed the right word(with the help of the word guesser function), but only for fight times. I will pass in the five different sets of both secret word and the hints 

print('Hello! Welcome to the WordGuesser Game! Are you ready to play!?')
#user have to enter y or n to play or not
start = input("Enter 'y' if you want to start playing or 'n' if you don't want to:")
#if the user are stupid :')
if start != 'y' and start != 'n':
    print("Arr, you have to enter only 'y' or 'n' buddy. ")
#if user doesn't want to play
elif start == 'n':
    print("Very Well. See you soon.....")
#if user wants to play
elif start == 'y':
    print("Ohh! Daring today, are we?Allright, let's get started!")
    print("Rules are simple:-->")
    print("1:You can get infinite amount of attempts. The attempts are gonna be counted.")
    print("2:You can ask for hint if you can't guess it just right yet(just after guess 10 times!).")
    print("3:A medium hint will auto show up if you can't guess it for 10 attempts.")
    print("4:A large hint will appear if you can't guess it at all and enter 'hint'")
    print("5:If you don't want to continue playing, you can enter 'stop' and it will stop.")
    print("6:If you want to restart, you can enter 'restart'. If you restart, your total number of attempts will be reset as well.")
    print("7:You have to capitalize the first letter of the word you guess")
    print("8:There're five levels which you can play where the difficulty will increase per each level.")
    print("9:Enjoy your time playing :)")
    #writing the function which will take the word and the hints as the input
    def word_guess(word, small_hint, medium_hint, big_hint):
        attempt = 0
        while True:
            user_guess = input("You can start guessing. The hint is '"+small_hint+"':")
            attempt = attempt +1
            if user_guess == word:
                print("Hazzah! You got it. The secret word is '"+word+"'!")
                break
            elif user_guess[0] == word[0]:
                print("Wow! You have got the first letter right! Keep it up.")
            elif user_guess == 'stop':
                print("Ok")
                attempt = attempt - 1
                break
            elif user_guess == 'restart':
                print("Restarting......")
                print("Here we go again!")
                print("Total attempts reset to '0'.")
                attempt = 0
                continue
            
            elif attempt < 5:
                print("Hmmm. Not quite right. Let's try again.")
            elif attempt >= 5 and attempt <=10:
                print("Come on! You're close!")
            elif attempt > 10:
                print("Alright! Here's another hint for your ease: '"+medium_hint+"'.")
            if user_guess == 'hint' and attempt > 10:
                    print("Okay, the big hint is '"+big_hint+"'.")
            elif user_guess == 'hint' and attempt <=10:
                    print("Sorry, you can ask for a hint only after attempting at least 10 times to guess. :')")
                    

        print("Total number of attempts you took:", attempt)
        if attempt == 1:
            print("You got it first try!!! That was super amazing!")
        elif attempt > 1 and attempt <= 5:
            print("Wow! You guessed the word with only "+str(attempt)+" attempts! Amazing!")
        print("I hope you enjoyed playing!")
    #asking if the user wants to play level 1
    play_1 = input("So shall we get started with the first level then? Enter 'yes' or 'no':")
    if play_1 == 'no':
        print("Hmmm. Quitting right from the start, are we? Fineeee. Please do come back tho.")
    elif play_1 == 'yes':
        print("Alright! Let's goooo!")
        print("Word-Guesser: Level 1")
        word_guess('China', 'A country', 'A country in Asia', 'The country being hated by globally since the start of 2020 due to the pandemic')
     #asking if the user wants to play the level 2
    play_2 = input("Do you want to play the next level? Enter 'yes' or 'no':")
    if play_2 == 'no':
            print("Alright. Farewell")
    elif play_2 == 'yes':
            print("Ahh! A true challenger I see. Be aware that the difficulty will increase. Good luck!")
            print("Word-Guesser: Level 2")
            word_guess('C++', 'It is a programming language', 'It is object-oriented compatible', 'It is used in game developments!')
    #level 2 done
    #level 3
    play_3 = input("Do you want to play the next level? Enter 'yes' or 'no':")
    if play_3 == 'no':
        print("Alright! See you at level 3 soon!")
    elif play_3 == 'yes':
        print("Woohooo! Keep the guessing train going! Advancing to level 3 here we go!!")
        print("Word-Guesser: Level 3")
        word_guess('College', 'It is related to education', 'It usually has many people wearing uniforms', 'Most of the ones who went there owe money to it')
    #level 4
    play_4 = input("Okay! You've come this far! Might as well go to next level, right? Enter 'yes' or 'no':")
    if play_4 == 'no':
        print("Awwwn! Don't wanna guess anymore? Fineeeee. Take a break of course.")
    elif play_4 == 'yes':
        print("Damnn! You never stop, do you? Love your enthusiasm! Alright! Thank you, next level :')")
        print("Word-Guesser: Level 4")
        word_guess('Arch Linux', 'An operating system', 'Open source and popular', 'I use it btw :)')
    #level 5
    play_5 = input("So, what'd you say if we move on to the final level? It's not that difficult I promise lol. 'yay' or 'nay':")
    if play_5 == 'nay':
        print("Understandable, have a nice day :')")
    elif play_5 == 'yay':
        print("Yess! That's the spirit. Here we gooo!")
        print("Word-Guesser: Level 5(Finale)")
        word_guess('Wozniak','Last name of a person','Related to a popular phone company', 'Apple')
        print("Oops! You beat me. There're no more levels available. But there may be soon so tune in. Byeee for now!")
    

    
        




        