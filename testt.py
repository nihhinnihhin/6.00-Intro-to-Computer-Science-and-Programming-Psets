#%%
def search(s, e):
    answer = None 
    i = 0
    numCompares = 0
    while i < len(s) and answer == None:
        numCompares += 1
        if e == s[i]:
            answer = True 
        elif e < s[i]:
            answer = False 
            i += 1
            print answer, numCompares

#%%
"""
linear
"""
def exp1(a,b):
    ans=1
    while(b>0):
        ans*=a
        b-=1
    return ans
#%%
def exp2(a,b):
    if b==1:
        return a
    else: return a*exp2(a,b-1)
#%%
def exp3(a,b):
    if b==1:
        return a
    if (b%2)*2==b:
        return exp3(a*a,b/2)
    else: return a*exp3(a,b-1)
#%%
sumDigits=0
for c in str(1952):
    sumDigits+=int(c)
print(sumDigits)
#%%
x=16
ans=0
while ans*ans<=x:
    ans=ans+1
print(ans)
#%%
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
#%%
x = int(input("Please enter a number: "))
#%%
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
#%%
f=open('workfile','rb+')
f.write(b'0123456789abcdef')
f.seek(5)
f.read(1)
f.seek(-3,2)
f.read(1)
#%%
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
#%%
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)
#%%
for i,v in enumerate(['i','love','you']):
    print(i,v)
#%%
matrix=[[2,3,1,4,-9],[1,1,1,1,-3]\
       ,[1,1,1,2,-5],[2,2,2,3,-8]]
i=0
[row[i] for row in matrix]
#%%
def extendList(val, list=[]):
    list.append(val)
    return list
#%%
list1 = extendList(10)  
list2 = extendList(123)
list3 = extendList('a')
#%%
print ("list1 = %s" ,list1)
print ("list2 = %s" ,list2)
print ("list3 = %s" , list3)
#%%
id(list1)
id(list2)
id(list3)
#%%
letter = "hai sethuraman"
for i in letter:
    if i == "a":
        pass
        print("pass statement is execute ..............")
    else:
        print(i)
#%%
import os
print (os.path.expanduser('~'))
#%%
A = [[None] * 2] * 3
for i in range(6):
        id(A[i])
#%%
#words = ['cat', 'window', 'defenestrate']
for w in words:
    if len(w)>6:
        words.insert(0,w)
#%%
words=['algorithm','program','computer','robotic']
for w in words:
    if len(w)>8:
        words.insert(0,w)
#%%
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
#%%
i = 5
def f(arg=i):
    print(arg)
i = 6
f()
#%%
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
#%%
def parrot(voltage, state='a stiff', action='voom', \
           type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword    

parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
    
#%%    
def combination() 
#%%    
stack=[1,2,3,4,5] 
queue=deque(stack,8)
    
    
    
    
    
    