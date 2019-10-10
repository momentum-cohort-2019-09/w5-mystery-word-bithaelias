import random
def main():
    with open('words.txt') as file:
        text = file.read()
        all_words = text.split()
    incorrect_guesses = []
    correct_guesses = []
    easy_mode = []
    normal_mode = []
    hard_mode = []
    guesses = []
    
    for word in all_words:
        if len(word) >= 4 and len(word) <= 6:
            easy_mode.append(word)
        elif len(word) > 6 and len(word) <=8:
            normal_mode.append(word) 
        elif len(word) > 8:
            hard_mode.append(word)   

    def start_game():
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
        user_input = input('Guess a letter: ')
        for letter in word:
            if letter in guesses:
                display.append(letter)

    start_game()
    
    # def display_letters(word,guesses): 
   
    #     display =[]
    #     
    #         else:
    #             display.append('_')
    #     return display   


   
        
        

# while len(guesses) <= 8:
#         
#         guesses.append(user_input)
#         display = display_letters(word,guesses)  
#         print(display)


    

   
    

        
# def display_underscores():
#     random_word = display_random_word()       
#     print('_ '* len(random_word)) 
#     print(random_word)


# start_game()

# word = display_random_word()
# print(word)
main()

# difficulty()
# display_underscores()


