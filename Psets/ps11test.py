# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 16:41:27 2018

@author: 18566
"""

def testHarness():
    x,y=5,6
    pos=Position(x,y)
    angle=90
    speed=1
#    if pos.getX()!=5:
##        raise ValueError('in Position.getX')
#        print('in Position.getX')
#    elif pos.getY()!=6:
##        raise ValueError('in Position.getY')
#    elif pos.getNewPosition(angle,speed)!=Position(6,6):
##        raise ValueError('in Position.getNewPosition')
#    else:print('-------------Successed---------')
    if pos.getX()==5 and pos.getY()==6 and pos.getNewPosition(angle,speed)==Position(6,6):
        print('-------------Successed---------')
    else:print('-------------Failure--------')

def test_all():
    testHarness()
    
test_all()