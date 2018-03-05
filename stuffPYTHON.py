
word = list("python")

def start():
    print("Hello! Welcome to Hangman!")
    name = input("What's your name? ")
    print("Welcome ", name, "!")
    yes_or_no()

def yes_or_no():
    choice = input("Would you like to play Hangman? (Yes/No) :")
    if choice == "Yes":
        print("Let's begin!")
        print("")
        goal()
    elif choice == "No":
        print("That's too bad... Maybe another time!")
        print("")
        start()
    else:
        print("Please type Yes or No...")
        yes_or_no()

def goal():
    print("Your goal is to find a word by guessing letters!")
    begin()
    
def begin():
    guess = input("Please guess a letter (lowercase): ")
    if guess == "p":
        del(word[0])
        print("That is a correct letter!")
        if word == []:
            winner()
        else:
            begin()
            
    elif guess == "y":
        del(word[0])
        print("That is a correct letter!")
        if word == []:
            winner()
        else:
            begin()
            
    elif guess == "t":
        del(word[0])
        print("That is a correct letter!")
        if word == []:
            winner()
        else:
            begin()
            
    elif guess == "h":
        del(word[0])
        print("That is a correct letter!")
        if word == []:
            winner()
        else:
            begin()
            
    elif guess == "o":
        del(word[0])
        print("That is a correct letter!")
        if word == []:
            winner()
        else:
            begin()
            
    elif guess == "n":
        del(word[0])
        print("That is a correct letter!")
        if word == []:
            winner()
        else:
            begin()
    else:
        print("Wrong letter!")
        begin()
        
        
def winner():
    print("")
    print("You WIN!!!")
    print("")
    start()
    
start()










