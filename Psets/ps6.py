# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
# Do some MODIFICATIONs to run the code successfully
# Look up what modification have been made by searching "MODIFICATION"


import random
import string
import time

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
    print('Current Hand:',end=' ')
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
# Problem #2.3: Computer Player
#
def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value.
    
    return: string->int
    """
    points_dict={word:get_word_score(word,HAND_SIZE) for word in word_list}
    return points_dict

def get_time_limit(points_dict,k):
    """
    Return the time limit for the computer player as a function of 
    the multiplier k.
    
    points_dict should be the same dictionary that is created by 
    get_words_to_points.
    """
    start_time=time.time()
    # Do some computation... The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known a task.
    for word in points_dict:    # this statement would get the key of the dict
        get_frequency_dict(word)
        get_word_score(word,HAND_SIZE)
    end_time=time.time()
    return (end_time-start_time)*k

#%%
def pick_best_word(hand,points_dict):
    """
    Return the highest scoring word from points_dict that can be made
    with the given hand
    
    Return '.' if no words can be made with the given hand.
    """
    next_word=0
    for i in points_dict:   # assign the first key of points_dict to h_word
        h_word=i
        break
    for word in points_dict:    # it's better to directly use the is_valid_word to check
        hand_copy=hand.copy()   # every round should reset the hand_copy
                                # or else all the words check use the same hand.copy
        for letter in word:
            hand_copy[letter]=hand_copy.get(letter,0)-1
            # the function is similar to update_hand.
            # when the letter is not in the hand,
            # hand_copy[letter] will the value of (0-1)=-1
            if hand_copy[letter]<0:
                next_word=1
        if next_word==1: 
            next_word=0
            continue
        if points_dict[h_word]<points_dict[word]:
            h_word=word
    return h_word
    
def test_pick_best_word():
    """
    To test the pick_best_word
    the correct result should be 'abc'
    """
    testhand={'a':2,'b':2,'c':2}
    testPdict={'a':1,'ab':2,'abc':3}
    pick_best_word(testhand,testPdict)
#%%
def pick_best_word_faster(hand,rearrange_dict):
    '''
    return the highest-scoring word
    
    hand: dict
    rearrange_dict: sting->string
    return: string
    
    psuedo code
    To find some word that can be made out of the letters in HAND:
        For each subset S of the letters of HAND:
            Let w=(string containing the letters of S in sorted order)
            if w in d: return d[w]
    '''
    hand_string=''
    highest_scoring_word='aa'
    for letter in hand.keys():
        for j in range(hand[letter]):
            hand_string+=letter        
    submultisets=build_substrings(hand_string)
    for w in submultisets:
        if w in rearrange_dict:
            candidate=rearrange_dict[w]
            if points_dict[candidate]>points_dict[highest_scoring_word]:
                highest_scoring_word=candidate
    return highest_scoring_word
    
def build_substrings(string):
    """
    Works on the premiss that given a set of the substrings of a string the
    the subsets of a string with one more char is the formed by taking all the
    substrings in the known subset and also adding to them the set formed by
    adding the character to every element in the old set and then adding the 
    new char.
    
    string: string
    return: list
    """
    result = []
    if len(string) == 1:
        result.append(string)
    else:
        for substring in build_substrings(string[:-1]):
            result.append(substring)
            substring = substring + string[-1]
            result.append(substring)
        result.append(string[-1])
        result = list(set(result))  # Convert result into a set.  Sets have no duplicates. Then convert back to list.
        result.sort()
    # now iterate through substrings and sort the characters of each substring    
    #for each in 
    return result

def get_word_rearrangements(word_list):
    '''
    return rearrangement of word in word_list
    
    word_list: list of string
    
    psuedo code
    Let d={}
    For every word w in the word list:
        Let d[(string containing the letters of w in sorted order)]=w
    '''
    rearrange_dict={}
    for w in word_list:
        rearrange_dict[''.join(sorted(w))]=w
    return rearrange_dict


def sort_word(word_string):
    """
    Takes a string, alphabetizes it and returns it as a string.
    
    first convert the string to  a list, then sort it, and concert it 
    again
    
    word:word_string
    return: string
    """
    char_list =[]
    sorted_string = ''
    for char in word_string:
        char_list.append(char)
    char_list.sort()
    for char in char_list:
        sorted_string += char
    return sorted_string

    
# =============================================================================
# def find_subsets(string):
#     '''
#     return all the sub-multisets of hand ->list of string
#     
#     string: string
#     '''
# #    hand={'a':1,'b':1,'c':1}   # used to test
#     sub_multisets=[]
#     for i in range(1,len(string)+1):
#         print(i)
#         sub_multisets+=find_n_combinations(string,i)
#     return sub_multisets
# 
# 
# def find_n_combinations(hand,n):
# #    print(hand_copy)
#     '''
#     the function implement by recursive way, a little bit different
#     from Hanoi Tower problem, all of the primitive step(base problem step)
#     are included in the function, which means in the else_block_of_code, 
#     there are just function invocation statements.
#     
#     return list of all combinations of n elements of hand
#     
#     psuedo code:
#         if n==2:
#             for every string s in hand:
#                 combine s with post letter in hand
#                 concatenate the result to subsets
#                 return subsets
#         if n>2:
#             for every string s in subsets(find_n_combinations(hand,n-1)):
#                 combine s with post letter in hand
#                 return subsets
#                 
#     e.g. 
#     >>>find_n_combinations(abcd',3)
#     >>>['abc', 'abd', 'acd', 'bcd']
#     
#     hand: string
#     n: int
#     '''
#     hand_copy=''.join(sorted(hand))
#     # Hit the beginning of the list.
#     if n==2:
#         subsets=[]
#         last_list=list(hand_copy)
#         for i in range(len(last_list)-1):
#             element=last_list[i]
#             position=hand_copy.find(element[len(element)-1])
# #            print(position)
#             for j in range(position+1,len(hand_copy)):
#                 s=element+hand_copy[j]
#                 subsets.append(s)
# #                print(s)
#         return subsets
#     else:
#         subsets=[]
#         last_list=find_n_combinations(hand,n-1)
#         for i in range(len(last_list)-1):
#             element=last_list[i]
#             position=hand_copy.find(element[len(element)-1])
# #            print(position)
#             for j in range(position+1,len(hand_copy)):
#                 s=element+hand_copy[j]
#                 subsets.append(s)
# #                print(s)
#         return subsets
#        
# # =============================================================================
# # def find_n_combinations(hand,n):
# # #    print(hand_copy)
# #     hand_copy=''.join(sorted(hand))
# #     if n==2:
# #         subsets=[]
# #         for i in range(len(hand_copy)-1):
# #             for j in range(i+1,len(hand_copy)):
# #                 s=hand_copy[i]+hand_copy[j]
# # #                print(s)
# #                 subsets.append(s)
# #         return subsets
# # #    print(subsets)
# #     else:
# #         subsets=[]
# #         last_list=find_n_combinations(hand,n-1)
# #         for i in range(len(last_list)-1):
# #             position=hand_copy.find(last_list[len(last_list[i])-1])
# #             for j in range(position+1,len(hand_copy)):
# #                 s=last_list[i]+hand_copy[j]
# #                 subsets.append(s)
# # #                print(subsets)
# #         return subsets
# #         
# # =============================================================================
#     
# =============================================================================
        
    
#%%
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
        av_total_score=0
        while True:
            try:
                limit_time=int(input('Enter time limit, in seconds, for players:'))
                break
            except ValueError:
                print("Oops!  That was not integer.  Try again...")
        display_hand(hand)
        remaining_time=limit_time
        HandLetNum=0
        while True:
            while True: # the loop is used to ask user for a valid word
                # calculate the time taken to provide an answer
                start_time=time.time()
                word=str(input('Enter word, or a . to indicate that you are finished: '))
                end_time=time.time()
                total_time=end_time-start_time
                remaining_time-=total_time
                print('It took {0:.2f} seconds to provide an answer'.format(total_time))
                if remaining_time<=0:
                    print('Total time exceeds {0} seconds. You scored {1:.2f} points'.format(limit_time,av_total_score))
                    raise KeyboardInterrupt
                print('You have {0:.2f} seconds remaining'.format(remaining_time))
                if word=='.':raise KeyboardInterrupt    # when player enter dot
                if is_valid_word(word,hand,word_list):  # game will be exited
                    break
                else:  print("Oops!  That was no valid word.  Try again...")
            av_score=get_word_score(word,n)/total_time    
            hand=update_hand(hand,word)
            av_total_score+=av_score
            print('{0} earned {1:.2f} points. Total: {1:.2f} points\n'\
                  .format(word,av_score,av_total_score),end='')
            display_hand(hand)
            for k,v in hand.items():    # calculate the number of letters left
                                        # to decide whether the game is finished
                HandLetNum+=v
            if HandLetNum==0:
                print('Game finished. Your final score is {0} points'.format(av_total_score))
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
    points_dict=get_words_to_points(word_list)  
    k=1
    time_limit=get_time_limit(points_dict,k)
    rearrange_dict=get_word_rearrangements(word_list)
                    # how many times the function get_words_to_points would be called once per(game, hand,turn?)
                    # think of how often this get_time_limit should be called. Define a global
                    # variable time_limit to store the result of the function
