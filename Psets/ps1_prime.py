# -*- coding: utf-8 -*-
# =============================================================================
# Problem Set 0
# Name: Hin Mo
# Collaborators: Laplace
# Time:unknown
# =============================================================================
   
#%%
'''
find the nth prime number using brute force
'''

# =============================================================================
# optimization
# 1 Even number except 2 is not prime number
# 2 For suffiently n, the product of prime numbers less than n is less than
# or equal to e**n and as n grows, the ratio, i.e. product/(e**n)≈1
# 
# =============================================================================
def find(n):
    count=1
    num=2
    flag=0
    while True:
        if n==1:
            print('the {0}th prime number is {1}'.format(count,num))
            break
        if num==2: #assert statement
            num+=1
            count+=1
            continue
        for i in range(2,num):
            if num%i==0:
                flag=0
                break
            else: flag=1
        if flag==1:
            if count==n:
                print('the {0}th prime number is {1}'.format(count,num))
                break
            count+=1
        num+=2 