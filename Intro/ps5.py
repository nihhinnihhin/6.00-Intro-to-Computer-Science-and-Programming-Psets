# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
# Do some MODIFICATIONs to run the code successfully
# Look up what modification have been made by searching "MODIFICATION"

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 9

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
        # ??? what is the specification of the statement above?
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
        # ???what is the specification of the statement above
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
#    assert str.isalpha(word),'all of the characters in the string you enter should be letters, and should contain other type, but lowercase and uppercase are the same'
    # missing the situation where string contains ' ', waiting for modifying
#    assert type(n)==type(1),'please enter an integer for the argument n, not other type'+type(n)
#    str.lower(word)
#    str.islower()
#    Return true if all cased characters [4] in the string are lowercase and there is at least one cased character, false otherwise.
#    str.lower()
#    Return a copy of the string with all the cased characters [4] converted to lowercase.
    points=0
    letters_freq=get_frequency_dict(word)   # get the dictionary of frequency of the word
    for letter,freq in letters_freq.items():    # looping techniques
        points+=SCRABBLE_LETTER_VALUES[letter]*freq
    if len(word)==n:    # if all given letters are used at one time, add 50points
        points+=50
    return points

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print( letter,end=' ')             # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(n / 3) # MODIFICATION:the original is: num_vowels = (n / 3) 
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    hand_copy=hand.copy()
    for letter in word:
        hand_copy[letter]=hand_copy.get(letter)-1   
        # subtract the value of the correspoing letter of word in hand_copy by1
    return hand_copy
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    hand_copy=hand.copy()
    for letter in word:
        hand_copy[letter]=hand_copy.get(letter,0)-1
        # the function is similar to update_hand.
        # when the letter is not in the hand,
        # hand_copy[letter] will the value of (0-1)=-1
        if hand_copy[letter]<0:
            return False
    if word not in word_list:
        return False
    return True

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    try:    
    # use try-except to implement the function that exit the game whenever enter '.'
        n=len(hand)
        total_score=0
        print('the game is started')
        display_hand(hand)
        HandLetNum=0
        while True:
            while True: # the loop is used to ask user for a valid word
                word=str(input('please enter a valid word obeying the rules, like: word\n'))
                if word=='.':raise KeyboardInterrupt
                if is_valid_word(word,hand,word_list):
                    break
                else:  print("Oops!  That was no valid word.  Try again...")
            score=get_word_score(word,n)
            hand=update_hand(hand,word)
            total_score+=score
            print('the score of the current word is {0} points\
                  \nthe total score is {1} points'\
                  .format(score,total_score))
            display_hand(hand)
            for k,v in hand.items():    # calculate the number of letters left
                                        # to decide whether the game is finished
                HandLetNum+=v
            if HandLetNum==0:
                print('Game finished. Your final score is {0} points'.format(total_score))
                break
    except KeyboardInterrupt:
        print('Game Exited')

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
#    print ("play_game not implemented.")         # delete this once you've completed Problem #4
#    play_hand(deal_hand(HAND_SIZE), word_list) # delete this once you've completed Problem #4
    
    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print()
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print()
        elif cmd == 'e':
            break
        else:
            print ("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

