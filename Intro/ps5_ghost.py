# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print( "Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print( "  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

    
def play_ghost_game(wordlist):
    try:
        CurFrag=''
        print('Welcome to Ghost!')
        print('Player 1 goes first.')
        print('Current word fragment:\'\'')
        letter=input('Player 1 says letter: ')
        CurFrag+=letter

        while True:
            print('Current word fragment:\'{0}\''.format(CurFrag))
            print('Player 2\'s turn.')
            CurFrag=call_player_and_update_fragment(2,CurFrag,wordlist)
                
            print('Current word fragment:\'{0}\''.format(CurFrag))
            print('Player 1\'s turn.')
            CurFrag=call_player_and_update_fragment(1,CurFrag,wordlist)
            
    except KeyboardInterrupt:
        print('Game end')
        
def call_player_and_update_fragment(PlayNum,CurFrag,wordlist):
    """
    Print the message including current word fragment,
    ask the alternately turnplayer to type a letter
    
    PlayNum: int
    CurFrag: string
    wordlist: list of string
    """
    print('Current word fragment:\'{0}\''.format(CurFrag))
    print('Player {0}\'s turn.'.format(PlayNum))
    while True: # the loop is used to ask user for a valid word
        letter=str.lower(input('Player {0} says letter: '.format(PlayNum)))
        if letter=='.':raise KeyboardInterrupt      # player could type '.' to exit the game at any timme
        if letter in string.ascii_letters:
            break
        else:  print("Oops!  That was no valid word.  Try again...")
    CurFrag+=letter
    LoseReason=cannot_add(CurFrag,wordlist)
    if LoseReason>0:
        final_message(PlayNum,LoseReason,CurFrag) 
    return CurFrag 

def cannot_add(CurFrag,wordlist):
    """
    return 0 if the CurFrag could be added continualy
    else if the CurFrag is in the wordlist, return 1, meaning one of the player lost the game
    else if no word starts with CurFrag, return 2, meaning one of the player lost the game
    
    CurFrag: string
    wordlist: list of string
    """
    for i in wordlist:
#        print(i[0:len(CurFrag)],CurFrag)
        if CurFrag==i[0:len(CurFrag)]:
            if len(CurFrag)==len(i):return 1
            else:return 0
    return 2

def final_message(Loser,LoseReason,FinalFrag):
    """
    print the message about who wins and who loses,
    and the reason
    
    Loser: int
    LoseReason: int
    FinalFrag: string
    """
    print('Current word fragment:\'{0}\''.format(FinalFrag))
    if Loser==1: 
        Winner=2
    else:
        Winner=1
    if LoseReason==1:
        print('Player {0} loses because \'{1}\' is a word!'.format(Loser,FinalFrag))
    else:
        print('Player {0} loses because no word begins with \'{1}\'!'.format(Loser,FinalFrag))
    print('Player {0} wins!'.format(Winner))
    raise KeyboardInterrupt
    
if __name__ == '__main__':
    play_ghost_game(wordlist)
