import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    This function returns a Boolean value: True if secret_word was guessed, and False otherwise.
    '''
    if set(secret_word) <= set(letters_guessed):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    This function returns a string consisting of letters and underscores based on which letters from letters_guessed are contained in secret_word.
    '''
    word_list = list()
    for i in secret_word:
        if i in letters_guessed:
            word_list.append(i)
        else:
            word_list.append('_ ')
    return ''.join(word_list)
    

def get_available_letters(letters_guessed):
    '''
    This function returns a string that contains lowercase letters of the English alphabet - all letters that are not in letters_guessed.
    '''
    abc = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in abc:
            abc.remove(i)
    return ''.join(abc)        
 

def hangman(secret_word):
    '''
    Game: Hangman
    '''    
    guesses = 6
    error = 3
    letters_entered = ''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secret_word)))
    print('You have 3 warnings left.')
    while True:
      if guesses > 0 and is_word_guessed(secret_word, letters_entered) == False:    
        print('-'*12)
        print('You have {} guesses left.'.format(guesses))    
        print('Available letters: {}'.format(get_available_letters(letters_entered)))
        letters = input('Please guess a letter: ').lower()
        if len(letters) == 1 and letters in get_available_letters(letters_entered):      
          letters_entered += letters
          if letters in secret_word:
            print('Good guess:',get_guessed_word(secret_word, letters_entered))
          else:
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_entered))    
            if letters in 'aieou':
              guesses -= 2
            else: 
              guesses -= 1
        elif len(letters)> 1 or len(letters) == 0 or letters not in string.ascii_lowercase:
          if error <= -1 or error == 'no':
            guesses -= 1    
          elif error >= 0:
            error -= 1
            if error == -1:    
              guesses -= 1
              error = 'no'        
          print('Oops! That is not a valid letter. You have {} warnings left: {}'.format(error, get_guessed_word(secret_word, letters_entered)))    

        elif letters in string.ascii_lowercase and letters not in get_available_letters(letters_entered):
          if error <= -1 or error == 'no':
              guesses -= 1    
          elif error >= 0:
            error -= 1
            if error == -1:    
              guesses -= 1
              error = 'no' 
          if error == 'no':
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {}".format(get_guessed_word(secret_word, letters_entered)))    
          else:             
            print("Oops! You've already guessed that letter. You have {} warnings left: {}".format(error, get_guessed_word(secret_word, letters_entered)))
      elif guesses > 0 and is_word_guessed(secret_word, letters_entered) == True:
        print('-'*12)    
        print('Congratulations, you won! Your total score for this game is: {}'.format(guesses*len(set(secret_word))))  
        break
      elif guesses <= 0: 
        print('-'*12)
        print('Sorry, you ran out of guesses. The word was {}'.format(secret_word))
        break        



def match_with_gaps(my_word, other_word):
    '''
     The function returns True if the guessed letters from my_word match the corresponding letters from other_word.
     It returns False if two words are different lengths or the guessed letters from my_word do not match the letters from other_word.
    '''
    my_word = my_word.replace(' ', '')
    list_my_word = list(my_word)
    list_other_word =list(other_word)
    set_my_word = set(my_word)
    set_my_word.difference_update('_')
    if len(my_word) == len(other_word):
        for i in set_my_word:
            if my_word.count(i) != other_word.count(i):
                return False
            for j in range(0, len(list_my_word)):
                if list_my_word[j] == '_':
                    continue
                if list_my_word[j] != list_other_word[j]:
                    return False   
        return True                
    else:
        return False 
    
              

def show_possible_matches(my_word):
    '''
    The function displays all words from the wordlist that fit my_word.
    '''
    appropriate_words = ''
    for i in range(0, len(wordlist)):
      if match_with_gaps(my_word, wordlist[i]) == True:
        appropriate_words += wordlist[i] + ' '
    if appropriate_words == '' or len(appropriate_words.split())> 25:
      return 'No matches found.'     
    else:
      return 'Possible word matches are: '+ appropriate_words         


    



def hangman_with_hints(secret_word):
    '''
    Game: Hangman with hints
    '''
    guesses = 6
    error = 3
    letters_entered = ''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secret_word)))
    print('You have 3 warnings left.')
    while True:
      if guesses > 0 and is_word_guessed(secret_word, letters_entered) == False:    
        print('-'*12)
        print('You have {} guesses left.'.format(guesses))    
        print('Available letters: {}'.format(get_available_letters(letters_entered)))
        letters = input('Please guess a letter: ').lower()
        if letters == '*':
          print(show_possible_matches(get_guessed_word(secret_word, letters_entered)))     
        elif len(letters) == 1 and letters in get_available_letters(letters_entered):      
          letters_entered += letters
          if letters in secret_word:
            print('Good guess:',get_guessed_word(secret_word, letters_entered))
          else:
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_entered))    
            if letters in 'aieou':
              guesses -= 2
            else: 
              guesses -= 1
        elif len(letters)> 1 or len(letters) == 0 or letters not in string.ascii_lowercase:
          if error <= -1 or error == 'no':
            guesses -= 1    
          elif error >= 0:
            error -= 1
            if error == -1:    
              guesses -= 1
              error = 'no'        
          print('Oops! That is not a valid letter. You have {} warnings left: {}'.format(error, get_guessed_word(secret_word, letters_entered)))    

        elif letters in string.ascii_lowercase and letters not in get_available_letters(letters_entered):
          if error <= -1 or error == 'no':
              guesses -= 1    
          elif error >= 0:
            error -= 1
            if error == -1:    
              guesses -= 1
              error = 'no' 
          if error == 'no':
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {}".format(get_guessed_word(secret_word, letters_entered)))    
          else:             
            print("Oops! You've already guessed that letter. You have {} warnings left: {}".format(error, get_guessed_word(secret_word, letters_entered)))
      elif guesses > 0 and is_word_guessed(secret_word, letters_entered) == True:
        print('-'*12)    
        print('Congratulations, you won! Your total score for this game is: {}'.format(guesses*len(set(secret_word))))  
        break
      elif guesses <= 0: 
        print('-'*12)
        print('Sorry, you ran out of guesses. The word was {}'.format(secret_word))
        break
   

if __name__ == "__main__":  
    while True:
      print('Enter 1 to play in hangman.\nEnter 2 to play in hangman with hints.')    
      number = input('Enter 1 or 2: ')
      if number == '1' or number == '2':
        break
    print('-'*12)  
    if number == '1':
      secret_word = choose_word(wordlist)
      hangman(secret_word) 
    else:
      secret_word = choose_word(wordlist)
      hangman_with_hints(secret_word)

