import random
# def main(word):



def start_game():
    permission = input('Would you like to guess a word, press y for yes and n for no:')
    if permission  == 'y':
        difficulty()
        display_random_word()
    else: 
        print('See you next time')

def difficulty():
    guess_difficulty = input('Press e for Easy mode, n for normal mode, or h for hard mode:').lower()
    if guess_difficulty == 'e':
        word_range = range(4,7)
        print("Welcome to easy mode")
    if guess_difficulty == 'n':
        word_range = range(6,9)
        print("You've entered normal mode")
    if guess_difficulty == 'h':
        word_range = range(8,30)
        print("Prepare for hard mode")



def display_letters(word,guesses): 
    # incorrect_guesses = []
    display =[]
    for letter in word:
        if letter in guesses:
            display.append(letter)
        else:
            display.append('_')
    return display        
        



        

def display_random_word():
    with open('words.txt') as file:
        text = file.read()
        words = text.split()
        word = random.choice(words)  
        # print(word)
        return word
        # word_length = len(word)
        # print(word_length)
        
        
def display_underscores():
    random_word = display_random_word()       
    print('_ '* len(random_word)) 
    print(random_word)


start_game()
guesses =[]
word = display_random_word()
print(word)
user_input = input('Guess a letter ')
guesses.append(user_input)

display = display_letters(word,guesses)
print(display)

# difficulty()
# display_underscores()


