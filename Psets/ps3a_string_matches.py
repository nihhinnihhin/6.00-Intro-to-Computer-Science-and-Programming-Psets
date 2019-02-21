# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 14:59:02 2018

@author: 18566
"""

# =============================================================================
# Problem Set 2
# Name: Hin Mo
# Collaborators: Laplace
# Time:2h17mins
# =============================================================================
#%%
def countSubStringMatch1(target, key):
    '''
    this function check char one by one using iterative way
    '''
    count=0         # used to count the number of the instances of key in target
    ibase=0         # used  to record the index of the target in the outside loop
    iloop=0         # used to record the index of the target in the inside loop
    lenkey=len(key)
    lentar=len(target)
    while ibase<lentar: # iterate the charcter that match the first char of key string
        iloop=ibase
        for j in range(lenkey): 
            # is it better to loop the length of sequence or loop the element
            # check if key completely match to one part of target
            if (key[j])!=(target[iloop]):   # mistake: mix the iloop and ibase together
                ibase+=1
                break
            iloop+=1
            if j==(lenkey-1):
                count+=1
                ibase+=lenkey
    print(count)
#%%    
def countSubStringMatch2(target, key):
    '''
    this function check the instance of key in target string by string, also iterative way
    '''
    lenkey=len(key)
    lentar=len(target)
    count=0
    i=0
    while i <lentar:
        if key==target[i:i+lenkey]: # check if the whole key match the instance in target from the start index i 
            i+=lenkey               # mistake: forget to plus the base(missing 'i+'), the previous version is 'target[i:lenkey]'
            count+=1
#            print(count)
        else: 
            i+=1
#            print(i)
    print(count)
#%%    
def countSubStringMatchRecursive(target,key):
    '''
    using recursive way: first divide it until get the base one
    and solve it 
    
    target: string
    key: string
    '''
    if len(key)==2:
        i=0
        count=0
        lentar=len(target)
        lenkey=len(key)
        while i<lentar:
            if key[0]==target[i]:
                if key[1]==target[i+1]:
                    count+=1
                    i+=lenkey
            i+=1
        print(count)
    else:countSubStringMatchRecursive(target,key[:(len(key)-1)])
