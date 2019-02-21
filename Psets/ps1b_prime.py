# -*- coding: utf-8 -*-
# =============================================================================
# Problem Set 1
# Name: Hin Mo
# Collaborators: Laplace
# Time:unknown
# =============================================================================
from math import *
def Sum(n):
    Sum=log(2)
    flag=0
    if n==2:
        ratio=Sum/2
        print('the sum of the logs of the primes\
              less than {0} is {1} and the ratio\
              of these two quantities is {2}'.format(n,Sum,ratio))
    else:
        for num in range(3,n,2):
            for i in range(2,num):
                if num%i==0:
                    flag=0
                    break
                else: flag=1
            if flag==1:
                Sum+=log(num)
        ratio=Sum/n
        print('the sum of the logs of the primes\
              less than {0} is {1}, and the ratio\
              of these two quantities is {2}'.format(n,Sum,ratio))