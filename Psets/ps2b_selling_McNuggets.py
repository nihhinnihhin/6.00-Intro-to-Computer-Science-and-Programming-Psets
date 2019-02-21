# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:47:03 2018

@author: 18566
"""

# =============================================================================
# Problem Set 2
# Name: Hin Mo
# Collaborators: Laplace
# Time:short
# =============================================================================
def find_largest(num,packages=(6,9,20)):
#    packages=input('please enter the package sizes you want, ordered from smallest to largest')
    n=1     # n is the possible number of McNuggets
    flag=0  # flag is used to mark whether current n is none-solution instance
    NoSolution=[]   # used to save target n
    Solution=[] # used to save solution-n
    count=0         # count the current index of solution n
    while n<num:
#    while True:
        coef_a=int(n/(packages[0]))+1     # n/6 is the number used to iteratively generate
        coef_b=int(n/(packages[1]))+1     # all feasible coefficients of a,b,c, for example
        coef_c=int(n/(packages[2]))+1
        for a in range(0,coef_a):   # brute force test,a,b,c are 
            for b in range(coef_b): # separately the coefficients of equation
                for c in range(coef_c):
                    if (packages[0]*a+packages[1]*b+packages[2]*c)==n:
                        flag=1
#        print(Solution)
        if flag:                 
            Solution.append(n)
#            print(count)
            if len(Solution)>=6:
                if (Solution[count]-Solution[count-5])==5:
                        # look if the current target n is the last value
                        # of six consecutive values of none-solution n
                        print('Given package sizes {0} {1}, and {2} ,the largest number of McNuggets that cannot be bought  in exact quantity is: {3}'\
                              .format(packages[0],packages[1],packages[2],NoSolution[len(NoSolution)-1]))
                        break
            count+=1
        else:
            NoSolution.append(n)
        n+=1
        flag=0
        #import math

    #    print(solution)
#        return solution