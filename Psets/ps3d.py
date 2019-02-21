# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 21:30:01 2018

@author: 18566
"""

def subStringMatchExactlyOneSub(target,key):
    ExactlyOneSub=()
    OneSub=subStringMatchOneSub(key,target)
    ExactMatch=subStringMatchExact(target, key)
    print(OneSub)
    print(ExactMatch)
    for i in OneSub:
        if i not in ExactMatch:
            ExactlyOneSub+=(i,)
            print(i)
    return ExactlyOneSub
        