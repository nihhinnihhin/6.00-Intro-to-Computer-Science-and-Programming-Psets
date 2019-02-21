# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:47:03 2018

@author: 18566
"""

# =============================================================================
# Problem Set 1
# Name: Hin Mo
# Collaborators: Laplace
# Time:1h30mins
# =============================================================================
def find_largest(num):
    n=1     # n is the possible number of McNuggets
    flag=0  # flag is used to mark whether current n is none-solution instance
    NoSolution=[]   # used to save target n
    Solution=[] # used to save solution-n
    count=0         # count the current index of solution n
    while n<num:
#    while True:
        coef_a=int(n/6)+1       # n/6 is the number used to iteratively generate
        coef_b=int(n/9)+1       # all feasible coefficients of a,b,c, for example
        coef_c=int(n/20)+1
        for a in range(0,coef_a):   # brute force test
            for b in range(coef_b):
                for c in range(coef_c):
                    if (6*a+9*b+20*c)==n:
                        flag=1
        if flag:                 
            Solution.append(n)  # save n that can pass the test
#            print(count)
#            print(Solution)
            if len(Solution)>=6:
                if (Solution[count]-Solution[count-5])==5:  
                        # mistake: index out of range  because missing 
                        # the situation where n=6(base element),then coef_a=1,so``````
                        # look if the current target n is the last value
                        # of six consecutive values of none-solution n
                        print('Largest number of McNuggets that cannot be bought in exact quantity: {0}'\
                              .format(NoSolution[len(NoSolution)-1]))
                        break
            count+=1
        else:
            NoSolution.append(n)    # save n that cannot pass the test
        n+=1
        flag=0  # reset the flag
        #import math

    #    print(solution)
#        return solution