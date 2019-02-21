# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 16:53:51 2018

@author: 18566
"""
# -*- coding: utf-8 -*-
# =============================================================================
# Problem Set 1
# Name: Hin Mo
# Collaborators: Laplace
# Time:30mins
# =============================================================================
def solve(n):
    import math
    solution=[]
    coef_a=math.ceil(n/6)
    coef_b=math.ceil(n/9)
    coef_c=math.ceil(n/20)
    for a in range(0,coef_a):
        for b in range(coef_b):
            for c in range(coef_c):
                if (6*a+9*b+20*c)==n:
                    solution.append(n)
#    print(solution)
    return solution