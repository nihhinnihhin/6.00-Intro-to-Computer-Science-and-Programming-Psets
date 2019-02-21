# -*- coding: utf-8 -*-
"""
based on pa3a.py
Created on Sat Apr 21 19:42:41 2018
@author: 18566
"""
# =============================================================================
# Problem Set 2
# Name: Hin Mo
# Collaborators: Laplace
# Time:45mins
# =============================================================================
#%%
def subStringMatchExact(target, key):
    '''
    this function returns a tuple of all starting points of a match of a 
    key string in a target string, not just the first instance
    '''
    if key=='':
        return tuple(range(len(target)))
    else:
        MatchIndex=()
        lenkey=len(key)
        lentar=len(target)
        count=0
        i=0
        while i <lentar:
            if key==target[i:i+lenkey]: # check if the whole key match the instance in target from the start index i 
                MatchIndex+=(i,)        # concatenate tuple
                i+=lenkey               # mistake: forget to plus the base(missing 'i+'), the previous version is 'target[i:lenkey]'
                count+=1
    #            print(count)
            else: 
                i+=1
    #            print(i)        
        return MatchIndex
    
#%%    
# =============================================================================
# target1 = 'atgacatgcacaagtatgcat'
# target2 = 'atgaatgcatggatgtaaatgcag'
# key10 = 'a'
# key11 = 'atg'
# key12 = 'atgc'
# key13 = 'atgca'
# tar_no=1    # variable that represents the number of target, e.g.1,2
# key_no=10   # variable that represents the number of key,e.g. 11,12,13
# target_tuple=(target1,target2)
# key_tuple=(key10,key11,key12,key13)
# for i in target_tuple:
#     for j in key_tuple:
#         print('the tuple of starting poingt of target{0} against key{1} is {2}'
#           .format(tar_no,key_no,subStringMatchExact(i,j)))
#         key_no+=1
#     key_no=10
#     tar_no+=1
# 
# =============================================================================
        
    
# =============================================================================
# answer is following:
# the tuple of starting poingt of target1 against key10 is (0, 3, 5, 9, 11, 12, 15, 19)
# the tuple of starting poingt of target1 against key11 is (0, 5, 15)
# the tuple of starting poingt of target1 against key12 is (5, 15)
# the tuple of starting poingt of target1 against key13 is (5, 15)
# the tuple of starting poingt of target2 against key10 is (0, 3, 4, 8, 12, 16, 17, 18, 22)
# the tuple of starting poingt of target2 against key11 is (0, 4, 8, 12, 18)
# the tuple of starting poingt of target2 against key12 is (4, 18)
# the tuple of starting poingt of target2 against key13 is (4, 18)
# 
# =============================================================================
