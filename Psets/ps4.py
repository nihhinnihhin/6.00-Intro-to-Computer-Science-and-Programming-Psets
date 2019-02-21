# Problem Set 4
# Name: Hin Mo
# Collaborators: Laplace
# Time: 2h30mins

#
#%%
# Problem 1
#
def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    # TODO: Your code here.
    assert years>=0, 'years should be grater than r equal to 0, not'+str(years)
    F=[0]
    for i in range(1,years+1):
        F+=[F[i-1]*(1+0.01*growthRate)+salary*save*0.01]
    return F
    
# =============================================================================
#     F=[0,0]
#     for i in range(1,(years+1)):
#         F+=[F[2*i-2]*(1+0.01*growthRate)+salary*save*0.01]  
#         F+=[F[2*i-1]+F[2*i]]
#         # the even index element save one year
#         # the odd index element save total
#     return F
# #%%
# =============================================================================
#%%
def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = -2
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print (savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.
#%%
#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    F=[0]
    years=len(growthRates)
    for i in range(1,years+1):
        F+=[F[i-1]*(1+0.01*growthRates[i-1])+salary*save*0.01]
    return F
#%%
def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print (savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#
#%%
def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.
    F=[savings]
    years=len(growthRates)
    for i in range(1,years+1):
        F+=[F[i-1]*(1+0.01*growthRates[i-1])-expenses]
    return F
    
#%%
def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

#
# Problem 4
#
#%%
def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.
    assert epsilon>0,'epsilon must be positive, not'+str(epsilon)
    preAmount=nestEggVariable(salary,save, preRetireGrowthRates)
    savings=preAmount[-1]
    high=savings
    low=0
    expenses=(high+low)/2
    postAmount=postRetirement(savings,postRetireGrowthRates,expenses)
    remaining=postAmount[-1]
    print(remaining-0)
    ctr=1
    expectedLoopTimes=50
    while abs(remaining)>epsilon and ctr<=expectedLoopTimes:
        if remaining>0:
            ctr+=1
            low=expenses
            expenses=(high+low)/2
            postAmount=postRetirement(savings,postRetireGrowthRates,expenses)
            remaining=postAmount[-1]
            print(remaining)
        elif remaining<0:
            ctr+=1
            high=expenses
            expenses=(high+low)/2
            postAmount=postRetirement(savings,postRetireGrowthRates,expenses)
            remaining=postAmount[-1]
            print(remaining)
    return expenses 
#%%
def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .001
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print (expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
