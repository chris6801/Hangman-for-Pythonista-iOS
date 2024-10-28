import console
console.clear()

console.set_color(0, 255, 0)

allowed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

hangmans = {
    0: '      |==|\n'
       '         |\n'
       '         |\n'
       '         |',
       
    1: '      |==|\n'
       '      O  |\n'
       '         |\n'
       '         |',
       
    2: '      |==|\n'
       '      O  |\n'
       '      |  |\n'
       '         |',
       
    3: '      |==|\n'
       '      O  |\n'
       '     \|  |\n'
       '         |',
       
    4: '      |==|\n'
       '      O  |\n'
       '     \|/ |\n'
       '         |',
       
    5: '      |==|\n'
       '      O  |\n'
       '     \|/ |\n'
       '     /   |',
       
    6: '      |==|\n'
       '      X  |\n'
       '     \|/ |\n'
       '     / \ |'    
}

GUESSES = 6
missed = 0
game_over = False
new_game = True
won = False

console.clear()

prev_guesses = []
wrong_guesses = ""

good_guess = False

s_word = ''
r_word = []

word_len = len(s_word)

'''
for i in range(word_len):
    if s_word[i] != ' ':
        r_word.append('_')
    elif s_word[i] == ' ':
        r_word.append(' ')
'''   

while not game_over:
    console.clear()
    
    if new_game:
        s_word = console.input_alert('Hangman!', 'Enter a word: ').lower()
        new_game = False
        
        word_len = len(s_word)

        for i in range(word_len):
            if s_word[i] != ' ':
                r_word.append('_')
            elif s_word[i] == ' ':
                r_word.append(' ')
    
    print(hangmans[missed])
    print('==================')
    print(wrong_guesses)
    print('==================')
    r_word_str = ''
    for letter in r_word:
        r_word_str += letter + ' '
    print(r_word_str)
    print('\n')
           
    attempt = input('pick a letter: ').lower()
    
    good_guess = False
    
    if len(attempt) > 1 or attempt not in allowed or attempt in prev_guesses:
        print('Guess again!')
        good_guess = True
        
    
    elif attempt not in prev_guesses:
        for i, letter in enumerate(s_word):
            if attempt == letter:
                r_word[i] = attempt
                good_guess = True
        prev_guesses.append(attempt)
        if not good_guess:
            wrong_guesses += attempt
        
    elif attempt in prev_guesses:
        print('You already guessed that!')
        
    if not good_guess:
        GUESSES -= 1
        missed += 1
        
    if '_' not in r_word and GUESSES > 0:
        print('You won!')
        won = True
        game_over = True
        
    elif GUESSES == 0:
        print(hangmans[missed])
        print('You lose!')
        game_over = True
    
    if game_over:
        console.clear()
        print(hangmans[missed])
        print('==================')
        print(wrong_guesses)
        print('==================')
        r_word_str = ''
        for letter in r_word:
            r_word_str += letter + ' '
        print(r_word_str)
        print('\n')
        
        new = console.alert('Hangman', 'New game? Y/N', 'Yes', 'No')
    
        if new == 1:
            new_game = True
            game_over = False
            print('lets go')
            s_word = ''
            r_word = []
        
    
