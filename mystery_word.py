import random
def get_words():
    with open('words.txt') as file:
        text = file.read()
        all_words = text.split()
    return all_words
    
   
def start_game():
    easy_mode = []
    normal_mode = []
    hard_mode = []
    all_words = get_words()
    for word in all_words:
        if len(word) >= 4 and len(word) <= 6:
            easy_mode.append(word)
        elif len(word) > 6 and len(word) <=8:
            normal_mode.append(word) 
        elif len(word) > 8:
            hard_mode.append(word) 
    permission = input('Would you like to guess a word, press y for yes and n for no:')
    if permission  == 'y':
        guess_difficulty = input('Press e for Easy mode, n for normal mode, or h for hard mode:').lower()
        if guess_difficulty == 'e':
            print("Great! Welcome to easy mode")
            word = random.choice(easy_mode)
            print(word)
            
        if guess_difficulty == 'n':
            print("Great! You've entered normal mode")
            word = random.choice(normal_mode)
            print(word)
        if guess_difficulty == 'h':
            print("Awesome! Prepare for hard mode")
            word = random.choice(hard_mode)
            print(word)
    else: 
        print('See you next time')

    display = ['_'] * len(word)  
    print(' '.join(display)) 
    play_game(word, display)      
    
     


def play_game(word, display):    
    user_input = input('Guess a letter: ')
    start = 0
    incorrect_guesses = []
    while len(incorrect_guesses) <= 8:

        if word.find(user_input, start) == -1:
            incorrect_guesses.append(user_input)
            print(incorrect_guesses)
        else:

            while word.find(user_input, start) != -1:
                index = word.index(user_input,start)
                start = index + 1 
                display[index] = user_input
            print(' '.join(display))
            breakpoint()
            # return display
            break
            

  

start_game()
   

    # keep_playing = true
    # while len(incorrect_guesses) <= 8:




           


        
    
     





