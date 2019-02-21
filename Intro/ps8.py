# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

BESTSET,BESTVALUE=0,1
subject_filename="smaller_subjects.txt"
    

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    subjects_dict={}
    for line in inputFile:
        line_copy=line.strip('\n')
        subject=line_copy.split(',')
        subjects_dict[subject[0]]=(int(subject[1]),int(subject[2]))
    return subjects_dict
#        print(type(line))
#        print( line)

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    
    subjects: dict(str->tuple)
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames=sorted(subjects)
#    subNames = subjects.keys()
#    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]    #??? what does it mean
        work = subjects[s][WORK]
#        print(val,work)
#        val = subjects[s][VALUE]
#        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print( res)

#%%
def test_printSubjects():
#    print(subjects)
    printSubjects(subjects)
#%%
def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2


#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    assert type(maxWork)==int
    best={}                     # subNames is a list of string in sorted order 
    subNames=sorted(subjects)   # apply selection_sort algorithm to subNames, 
    len_subNames=len(subNames)  # by camparing the value of the corresponding  
    for i in range(len_subNames-1):    # tuple 
        betIndx=i
        betName=subNames[i]
        for j in range(i+1,len_subNames):
            if comparator(subjects[subNames[j]],subjects[betName]):
                betIndx=j
                betName=subNames[j]
        temp=subNames[i]
        subNames[i]=subNames[betIndx]
        subNames[betIndx]=temp
#    print(subNames)
#        print(maxWork)
        if maxWork<=0:
            break
        elif subjects[betName][WORK]<=maxWork:
            best[betName]=subjects[betName]
            maxWork-=subjects[betName][WORK]
    return best

#%%
def test_greedyAdvisor():
#    printSubjects(short_subjects)
    greedyAdvisor(short_subjects,15,cmpValue)
    printSubjects(greedyAdvisor(long_subjects,15,cmpValue))
#%%
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    '''
    sort of like the build_substrings fucntion in ps6.py,
    the difference is the start condition of the functions
    this function is head-first condition, build_string is end=first
    after all, both these used recursive way
    
    in recursive way, what should be the argument in the function
    
    there two tasks for me:(suggest,just do the first, the second,especially leave it)
        1, mappint this problem to dynamic program problem, just need to find how to
        build corresponding momemorization and use it
        2, mapping to the old recursive way and figure out:
            there two choice, follow the steps: divide and conquer, find the base step
            set some print and run it , to look how the argument being passed
    '''
    global numCalls_bruteForce
    numCalls_bruteForce+=1
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:     
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime(maxWork):
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    startTime=time.time()
    best=bruteForceAdvisor(short_subjects, maxWork)
    endTime=time.time()
    totalTime=endTime-startTime
    printSubjects(best)
    print('time using: ',totalTime,'seconds')
#%%
    

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

# =============================================================================
# bruteForceTime(5)
# 
# Course  Value   Work
# ======  ====    =====
# 12.04   7       1
# 6.00    10      1
# 7.00    7       1
# 7.16    7       1
# 7.17    10      1
# 
# Total Value:    41
# Total Work:     5
# 
# time using:  0.761948823928833 seconds
# 
# bruteForceTime(10)
# 
# Course  Value   Work
# ======  ====    =====
# 12.04   7       1
# 15.01   7       1
# 2.03    6       1
# 24.12   6       1
# 6.00    10      1
# 7.00    7       1
# 7.16    7       1
# 7.17    10      1
# 7.18    10      2
# 
# Total Value:    70
# Total Work:     10
# 
# time using:  154.13586473464966 seconds
# 
# =============================================================================
#%%
def fastMaxVal(w,v,i,aW,memo):
    global numCalls
    numCalls=0
    numCalls+=1
    try: return memo[(i,aW)]
    except KeyError:
        if i==0:
            if w[i]<=aW:
                memo[(i,aW)]=v[i]
                print(i,aW,v[i])
                return v[i]
            else:
                memo[(i,aW)]=0
                print(i,aW,0)
                return 0
        without_i=fastMaxVal(w,v,i-1,aW,memo)
        if w[i]>aW:
            memo[(i,aW)]=without_i
            print(i,aW,without_i)
            return without_i
        else: with_i=v[i]+fastMaxVal(w,v,i-1,aW-w[i],memo)
        res=max(with_i,without_i)
        print(i,aW,res)
        memo[(i,aW)]=res
        return res

def maxVal0(w,v,i,aW):
    global memo
    memo={}
    return fastMaxVal(w,v,i,aW,memo)

#w=[5,3,2]
#v=[9,7,8]
#i=1
#aW=3
#maxVal0(w,v,i,aW)

#%%
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
#    i=len(tupleList)-3
#    best_tuple=[None,None]  # bestSubset=best_tuple[0] bestSubset alue=best_tuple[1]
    bestSubset,bestSubsetValue=dpAdvisorHelper0(tupleList, maxWork, 0,None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def dpAdvisorHelper0(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    global m
    m={}    # what should the key of memo be???
    return dpAdvisorHelper1(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork,m)
def dpAdvisorHelper1(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork,m):
    # Hit the end of the list.
    '''
    sort of like the build_substrings fucntion in ps6.py,
    the difference is the start condition of the functions
    this function is head-first condition, build_string is end=first
    after all, both these used recursive way
    
    in recursive way, what should be the argument in the function
    
    there two tasks for me:(suggest,just do the first, the second,especially leave it)
        1, mappint this problem to dynamic program problem, just need to find how to
        build corresponding memorization and use it
        2, mapping to the old recursive way and figure out:
            there two choice, follow the steps: divide and conquer, find the base step
            set some print and run it , to look how the argument being passed
        3,recode like the problem in knapsack, which is right-first and depth-first
        different from this problem, which is left-first and depth-first
    
    some hard point:
        1,what should the key of memo be?
        2,depth-first,left-first,right-first?
    '''
    try:return m[(i,subsetValue,subsetWork)][BESTSET],m [(i,subsetValue,subsetWork)] [BESTVALUE]
    except KeyError:
        global numCalls_dp
        numCalls_dp+=1
        if i >= len(subjects):
            if  bestSubset== None or subsetValue > bestSubsetValue:
                # Found a new best.
                m [(i,subsetValue,subsetWork)]   =subset[:],subsetValue
#                print(i,subsetWork,m [(i,subsetValue,subsetWork)]   )
                return subset[:], subsetValue
            else:
                m [(i,subsetValue,subsetWork)]   =bestSubset, bestSubsetValue
                # Keep the current best.
#                print(i,subsetWork,m [(i,subsetValue,subsetWork)]   )
                return bestSubset, bestSubsetValue
        else:
#            print(i)
            s = subjects[i]
            # Try including subjects[i] in the current working subset.
            if subsetWork + s[WORK] <= maxWork:     
                subset.append(i)
#                print('in',i,subset)
#                if subset==[3,4]:print('why')
                bestSubset, bestSubsetValue = dpAdvisorHelper1(subjects,
                        maxWork, i+1, bestSubset, bestSubsetValue, subset,
                        subsetValue + s[VALUE], subsetWork + s[WORK],m)
                subset.pop()
#                print('out',i,subset)
#            print(i,subset)
            bestSubset, bestSubsetValue = dpAdvisorHelper1(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue, subsetWork,m)
            m [(i,subsetValue,subsetWork)]   =bestSubset, bestSubsetValue
#            print(j,i,subsetWork,m [(i,subsetValue,subsetWork)]   )
            return bestSubset, bestSubsetValue
#
# Problem 3: Subject Selection By Brute Force
#

def dpTime():
    """
    Runs tests on FAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    trial_work = [8,10,15,30,45,60,90,120]    
    total_times = {}
    numCalls_dict={}
    for each in trial_work:
        numCalls_dp=0
        print('Trial for max workload of {0}.'.format(each))
        startTime=time.time()
        best=dpAdvisor(long_subjects, each)
        endTime=time.time()
        total_times[each] = round(endTime - startTime, 2)
        numCalls_dict[each]=numCalls_dp
        printSubjects(best)
    print ('total_times:{0}\nnumCalls_dict: {1}'.format(total_times,numCalls_dict))
#%%
def test_dpTime():
    dpTime()
def test_bruteForceTime():
    bruteForceTime(3,5)
#a=1
#b=2
#def m():
##    a=1
##    b=2
#    return a,b
#m={(1,2):(1,2)}
#m[(1,2)][0]
#m[(1,2)][1]

#
# Problem 4: Subject Selection By Dynamic Programming
#
# =============================================================================
# def dpAdvisor(subjects, maxWork):
#     """
#     Returns a dictionary mapping subject name to (value, work) that contains a
#     set of subjects that provides the maximum value without exceeding maxWork.
# 
#     subjects: dictionary mapping subject name to (value, work)
#     maxWork: int >= 0
#     returns: dictionary mapping subject name to (value, work)
#     """
#     # TODO...
#     
# 
# #
# # Problem 5: Performance Comparison
# #
# def dpTime():
#     """
#     Runs tests on dpAdvisor and measures the time required to compute an
#     answer.
#     """
#     # TODO...
# 
# =============================================================================
if __name__ == '__main__':
    long_subjects=loadSubjects(SUBJECT_FILENAME)
    short_subjects = loadSubjects(subject_filename)


# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
    
# MY PROGRAM RESULTS

# =============================================================================
# 
#  dpTime()
# 
# Trial for max workload of 8.
# Course  Value   Work
# ======  ====    =====
# 2.01    2       2
# 2.03    6       1
# 2.04    3       2
# 2.05    2       2
# 6.00    10      1
# 
# Total Value:    23
# Total Work:     8
# 
# time using:0.2541046142578125 seconds
# totally called function 68450 times
# Trial for max workload of 10.
# Course  Value   Work
# ======  ====    =====
# 2.00    5       9
# 6.00    10      1
# 
# Total Value:    15
# Total Work:     10
# 
# time using:0.3892951011657715 seconds
# totally called function 168040 times
# Trial for max workload of 15.
# Course  Value   Work
# ======  ====    =====
# 2.00    5       9
# 2.01    2       2
# 2.03    6       1
# 2.04    3       2
# 6.00    10      1
# 
# Total Value:    26
# Total Work:     15
# 
# time using:0.7706329822540283 seconds
# totally called function 362883 times
# Trial for max workload of 30.
# Course  Value   Work
# ======  ====    =====
# 2.00    5       9
# 2.01    2       2
# 2.02    1       17
# 6.00    10      1
# 7.17    10      1
# 
# Total Value:    28
# Total Work:     30
# 
# time using:2.310960054397583 seconds
# totally called function 964890 times
# Trial for max workload of 45.
# Course  Value   Work
# ======  ====    =====
# 2.00    5       9
# 2.01    2       2
# 2.02    1       17
# 2.03    6       1
# 2.04    3       2
# 2.05    2       2
# 2.06    2       1
# 2.07    1       1
# 2.08    5       5
# 2.09    5       2
# 6.00    10      1
# 7.00    7       1
# 7.06    4       1
# 
# Total Value:    53
# Total Work:     45
# 
# time using:4.819003105163574 seconds
# totally called function 2117444 times
# Trial for max workload of 60.
# Course  Value   Work
# ======  ====    =====
# 2.00    5       9
# 2.01    2       2
# 2.02    1       17
# 2.03    6       1
# 2.04    3       2
# 2.05    2       2
# 2.06    2       1
# 2.07    1       1
# 2.08    5       5
# 2.09    5       2
# 2.10    6       12
# 2.12    10      4
# 6.00    10      1
# 7.00    7       1
# 
# Total Value:    65
# Total Work:     60
# 
# time using:7.478945970535278 seconds
# totally called function 3939446 times
# Trial for max workload of 90.
# Course  Value   Work
# ======  ====    =====
# 2.00    5       9
# 2.01    2       2
# 2.02    1       17
# 2.03    6       1
# 2.04    3       2
# 2.05    2       2
# 2.06    2       1
# 2.07    1       1
# 2.08    5       5
# 2.09    5       2
# 2.10    6       12
# 2.11    9       19
# 2.12    10      4
# 3.00    1       10
# 6.00    10      1
# 7.00    7       1
# 7.06    4       1
# 
# Total Value:    79
# Total Work:     90
# 
# time using:14.104796886444092 seconds
# totally called function 7387588 times
# Trial for max workload of 120.
# Course  Value   Work
# ======  ====    =====
# 2.00    5       9
# 2.01    2       2
# 2.02    1       17
# 2.03    6       1
# 2.04    3       2
# 2.05    2       2
# 2.06    2       1
# 2.07    1       1
# 2.08    5       5
# 2.09    5       2
# 2.10    6       12
# 2.11    9       19
# 2.12    10      4
# 2.13    5       20
# 2.14    8       19
# 3.12    5       4
# 
# Total Value:    75
# Total Work:     120
# 
# time using:22.687673330307007 seconds
# totally called function 12775959 times
# =============================================================================


# =============================================================================
# RESULTS FROM GITHUB
# 
# Trial for max workload of 8.
# Course  Value   Work
# ======  ====    =====
# 12.04   7       1
# 15.01   7       1
# 2.03    6       1
# 24.12   6       1
# 6.00    10      1
# 7.00    7       1
# 7.16    7       1
# 7.17    10      1
# 
# Total Value:    60
# Total Work:     8
# 
# Trial for max workload of 10.
# Course  Value   Work
# ======  ====    =====
# 12.04   7       1
# 15.01   7       1
# 2.03    6       1
# 24.12   6       1
# 6.00    10      1
# 7.00    7       1
# 7.16    7       1
# 7.17    10      1
# 7.18    10      2
# 
# Total Value:    70
# Total Work:     10
# 
# Trial for max workload of 15.
# Course  Value   Work
# ======  ====    =====
# 12.04   7       1
# 14.02   10      2
# 15.01   7       1
# 2.03    6       1
# 22.03   10      2
# 24.12   6       1
# 6.00    10      1
# 7.00    7       1
# 7.06    4       1
# 7.16    7       1
# 7.17    10      1
# 7.18    10      2
# 
# Total Value:    94
# Total Work:     15
# 
# Trial for max workload of 30.
# Course  Value   Work
# ======  ====    =====
# 10.18   10      3
# 12.04   7       1
# 12.09   8       2
# 14.02   10      2
# 15.01   7       1
# 18.08   10      3
# 2.03    6       1
# 22.01   6       2
# 22.03   10      2
# 22.05   6       2
# 24.12   6       1
# 6.00    10      1
# 7.00    7       1
# 7.05    8       2
# 7.06    4       1
# 7.16    7       1
# 7.17    10      1
# 7.18    10      2
# 8.08    4       1
# 
# Total Value:    146
# Total Work:     30
# 
# Trial for max workload of 45.
# Course  Value   Work
# ======  ====    =====
# 10.18   10      3
# 12.04   7       1
# 12.09   8       2
# 14.02   10      2
# 14.17   9       3
# 15.01   7       1
# 18.08   10      3
# 18.12   9       3
# 2.03    6       1
# 22.01   6       2
# 22.03   10      2
# 22.05   6       2
# 22.06   10      3
# 24.12   6       1
# 6.00    10      1
# 6.17    9       3
# 7.00    7       1
# 7.05    8       2
# 7.06    4       1
# 7.16    7       1
# 7.17    10      1
# 7.18    10      2
# 8.08    4       1
# 9.03    9       3
# 
# Total Value:    192
# Total Work:     45
# 
# Trial for max workload of 60.
# Course  Value   Work
# ======  ====    =====
# 10.18   10      3
# 12.04   7       1
# 12.09   8       2
# 14.02   10      2
# 14.17   9       3
# 15.01   7       1
# 18.08   10      3
# 18.12   9       3
# 2.03    6       1
# 2.06    2       1
# 2.09    5       2
# 2.12    10      4
# 22.00   10      4
# 22.01   6       2
# 22.03   10      2
# 22.05   6       2
# 22.06   10      3
# 24.12   6       1
# 6.00    10      1
# 6.17    9       3
# 6.18    10      4
# 7.00    7       1
# 7.05    8       2
# 7.06    4       1
# 7.16    7       1
# 7.17    10      1
# 7.18    10      2
# 8.08    4       1
# 9.03    9       3
# 
# Total Value:    229
# Total Work:     60
# 
# Trial for max workload of 90.
# Course  Value   Work
# ======  ====    =====
# 10.18   10      3
# 12.04   7       1
# 12.09   8       2
# 14.02   10      2
# 14.10   9       4
# 14.17   9       3
# 15.01   7       1
# 18.08   10      3
# 18.12   9       3
# 2.03    6       1
# 2.09    5       2
# 2.12    10      4
# 22.00   10      4
# 22.01   6       2
# 22.02   7       3
# 22.03   10      2
# 22.04   7       3
# 22.05   6       2
# 22.06   10      3
# 24.12   6       1
# 6.00    10      1
# 6.12    6       3
# 6.17    9       3
# 6.18    10      4
# 7.00    7       1
# 7.04    10      5
# 7.05    8       2
# 7.06    4       1
# 7.12    8       4
# 7.16    7       1
# 7.17    10      1
# 7.18    10      2
# 7.19    10      5
# 8.08    4       1
# 9.03    9       3
# 9.14    9       4
# 
# Total Value:    293
# Total Work:     90
# 
# Trial for max workload of 120.
# Course  Value   Work
# ======  ====    =====
# 10.18   10      3
# 12.03   2       1
# 12.04   7       1
# 12.07   6       3
# 12.09   8       2
# 14.02   10      2
# 14.10   9       4
# 14.14   9       5
# 14.17   9       3
# 15.01   7       1
# 18.08   10      3
# 18.12   9       3
# 2.03    6       1
# 2.04    3       2
# 2.06    2       1
# 2.09    5       2
# 2.12    10      4
# 22.00   10      4
# 22.01   6       2
# 22.02   7       3
# 22.03   10      2
# 22.04   7       3
# 22.05   6       2
# 22.06   10      3
# 24.01   4       2
# 24.12   6       1
# 4.08    6       4
# 6.00    10      1
# 6.12    6       3
# 6.15    10      6
# 6.17    9       3
# 6.18    10      4
# 7.00    7       1
# 7.02    3       2
# 7.04    10      5
# 7.05    8       2
# 7.06    4       1
# 7.11    7       4
# 7.12    8       4
# 7.16    7       1
# 7.17    10      1
# 7.18    10      2
# 7.19    10      5
# 8.08    4       1
# 9.03    9       3
# 9.14    9       4
# 
# Total Value:    345
# Total Work:     120
# 
# total_times:{8: 0.0, 10: 0.01, 15: 0.0, 30: 0.02, 45: 0.02, 60: 0.09, 90: 0.04, 120: 0.11}
# numCalls_dict: {8: 0, 10: 0, 15: 0, 30: 0, 45: 0, 60: 0, 90: 0, 120: 0}
# =============================================================================
