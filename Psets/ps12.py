# 6.00 Problem Set 12
#
# Name:
# Collaborators:
# Time:
import time
import numpy
import random
import pylab

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """    

#
# PROBLEM 1
#

class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        # TODO
        self.maxBirthProb= maxBirthProb
        self.clearProb=clearProb
    def doesClear(self):
        """
        Stochastically determines whether this virus is cleared from the
        patient's body at a time step. 

        returns: Using a random number generator (random.random()), this method
        returns True with probability self.clearProb and otherwise returns
        False.
        """
        # TODO
        return random.random()<self.clearProb
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        # TODO
        reProb=self.maxBirthProb*(1-popDensity)
        if random.random()<reProb:
            return SimpleVirus(self.maxBirthProb,self.clearProb)
        else: raise NoChildException('In reproduce()')

class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.viruses=viruses
        self.maxPop=maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population. 

        returns: The total virus population (an integer)
        """
        # TODO 
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
          of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update() 

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
        # solution1:
#        i=0
#        while i <len(self.viruses):
#            print(self.getTotalPop(),i)
#            if self.viruses[i].doesClear():
#                self.viruses.pop(i)
#            else: i+=1
        # solution2:
#    		for index, virus in reversed( list( enumerate( self.viruses ) ) ):
#    			if virus.doesClear():
#    				# print( "Virus clears")
#    				# pop virus from viruses list
#    				self.viruses.pop( index )
        # solution3:
        for k,v in enumerate(self.viruses):
            if v.doesClear():
                self.viruses.pop(k)
        popDensity=len(self.viruses)/self.maxPop
        for j in range(len(self.viruses)):
            try:
                offspring=self.viruses[j].reproduce(popDensity)
                self.viruses.append(offspring)
            except NoChildException:
                continue

#
# PROBLEM 2
#

def problem2(num_trials):
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    

    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    # TODO
    popList=[]
    for j in range(num_trials):
        viruses=[]
        for k in range(100):
            viruses.append(SimpleVirus(0.1,0.05))
        patient=SimplePatient(viruses,1000)
        times=range(301)
        pop=[]
        for i in times:
            pop.append(patient.getTotalPop())
            patient.update()
        popList.append(pop)
    return popList,times

def simHelper():
    num_trials=10
    popList,times=problem2(num_trials)
    pop=computeMeans(popList)
    pylab.figure()
    line, = pylab.plot(times,pop, label='none')
    pylab.legend()
#    pylab.axis([0,30,0,4000])
    pylab.ylabel('time')
    pylab.xlabel('population of viruses in vivo')
    pylab.title('virus  population dynamics in vivo over {0} times simulations'
                .format(num_trials))
def test():
    simHelper()
     
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means
#print('\n'.join([''.join([('python!'[(x-y)%7]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

# PROBLEM 3
#

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """    
    
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        
        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        
        """
        # TODO
        self.maxBirthProb=maxBirthProb
        self.clearProb=clearProb
        self.resistances=resistances
        self.mutProb=mutProb
    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.        

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        # TODO
        return self.resistances[drug]
    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        # TODO
        # a flag to check whether the virus is resistant to all the drugs in
        # the prescription
        isResist=True   
        offResis=self.resistances.copy()
        for drug in activeDrugs:
            isResist=isResist and self.resistances.get(drug,True)
            # if a specific drug in the prescription is not in the resistance drugs 
            # list, that means this drug has no effect on the virus, i.e. 
            # the resistance of virus to this drug is True
        
        if isResist:    # reproduce
            if random.random()<(self.maxBirthProb * (1 - popDensity)):
                
                for k,v in offResis.items():    # mutation
                    if random.random()<self.mutProb:
                        offResis[k]=not offResis[k]
                return ResistantVirus(self.maxBirthProb,self.clearProb,
                                      offResis,self.mutProb)
        raise NoChildException

class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.viruses=viruses
        self.maxPop=maxPop
        self.adminDrugs=[]
        
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        if newDrug not in self.adminDrugs:
            self.adminDrugs.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        # TODO
        return self.adminDrugs
        
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # TODO
        popResisV=0
        for virus in self.viruses:
            isResist=True # this should be reset in every check of the virus
#            if type(virus)==ResistantVirus:
                # ??? is it right
                # the instance of superclass would not have the attribute of 
                # its subclass, but vice-versa, i.e. if a statement is  instance.attribute,
                # then it will directly override that of superclass, no matter how many arguments of the method
            for drug in drugResist:
                isResist=isResist and virus.getResistance(drug)
            if isResist: popResisV+=1
#            print(isResist,popResisV)
        return popResisV

    def update(self,timestep):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly
          
        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
#         first step, for each in viruses, clear?
        for k,v in enumerate(self.viruses):
            if v.doesClear():
                self.viruses.pop(k)
#        print('patient\'s list of viruses after clearance: {0}'.format(self.viruses))
        
        # calculate the current population density in the patient body
        popDensity=len(self.viruses)/self.maxPop
#        print('timestep:{0},total population after clearance: {1} resistant pop:{2}'.\
#              format(timestep,len(self.viruses),self.getResistPop(['guttagonol'])))
        
        # reproduce or not 
        for j in range(len(self.viruses)):
            try:
#                print('hhh')
                offspring=self.viruses[j].reproduce(popDensity,self.adminDrugs)
#                print('the resistance to guttagonol of offspring after reproduce:{0}',offspring.getResistance('guttagonol'))
                self.viruses.append(offspring)
            except NoChildException:
                continue

#
# PROBLEM 4
#

def problem4(num_trials,timesteps,addTime):
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO
    # create two list of list to record the population in every timestep in every simulations
    totPopList,resistPopList=[],[]
    maxBirthProb,clearProb,resistances,mutProb=0.1,0.05,{'guttagonol':False},0.005
    numViruses,maxPop=100,1000
    for j in range(num_trials):
        
        # reset a list of resistant viruses in every trial simulation
        viruses=[]
        for k in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb,clearProb,resistances,mutProb))
        patient=Patient(viruses,maxPop)
        totPop,resistPop=[],[]  # reset two list to record pop in every simulation
        
        # simulate over {0} timesteps
        for step in range(timesteps):
            if step==addTime:
##                print(patient.getPrescriptions())
                patient.addPrescription('guttagonol')
##                print(patient.getPrescriptions())
            totPop.append(patient.getTotalPop())
            resistPop.append(patient.getResistPop(['guttagonol']))
            patient.update(step)
        totPopList.append(totPop)
        resistPopList.append(resistPop)
    return totPopList,resistPopList

def Plot4(Ydata,Xlabel,Ylabel,Title,Legend=None):
    pylab.plot(Ydata, label=Legend)
    # Place a legend to the right of this smaller subplot.
    pylab.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # Place a legend above this subplot, expanding itself to
    # fully use the given bounding box.
#    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#               ncol=2, mode="expand", borderaxespad=0.)
    pylab.ylabel(Ylabel)
    pylab.xlabel(Xlabel)
    pylab.title(Title)
    

def testProblem4():
    num_trials,timesteps,addTime=5,300,150
    totPopList,resistPopList=problem4(num_trials,timesteps,addTime)
    totPop=computeMeans(totPopList)
    resistPop=computeMeans(resistPopList)
#    pylab.figure()
    Xlabel='time'
    Ylabel='population'
    Title='population of all virus and the resistant dynamics in vivo over {0} trials'.format(num_trials)
    totLegend='ptotal opulation'
    resistLegend='population of guttagono-\nresistant virus'
    Plot4(totPop,Xlabel,Ylabel,Title,totLegend)
    Plot4(resistPop,Xlabel,Ylabel,Title,resistLegend)

testProblem4()
#
# PROBLEM 5
#
##################################
def performSim(num_trials,preSteps,postStep):
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO
    # create two list of list to record the population in every timestep in every simulations
    totPopList,resistPopList=[],[]
    maxBirthProb,clearProb,resistances,mutProb=0.1,0.05,{'guttagonol':False},0.005
    numViruses,maxPop=100,1000
    for j in range(num_trials):
        
        # reset a list of resistant viruses in every trial simulation
        viruses=[]
        for k in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb,clearProb,resistances,mutProb))
        patient=Patient(viruses,maxPop)
        totPop,resistPop=[],[]  # reset two list to record pop in every simulation
        
        # simulate over {0} timesteps
        for step in range(preSteps+postStep):
            if step==preSteps:
##                print(patient.getPrescriptions())
                patient.addPrescription('guttagonol')
##                print(patient.getPrescriptions())
            totPop.append(patient.getTotalPop())
            resistPop.append(patient.getResistPop(['guttagonol']))
            patient.update(step)
        totPopList.append(totPop)
        resistPopList.append(resistPop)
    return totPopList,resistPopList

    
        
def problem5():
    """
    Runs simulations and make histograms for problem 5.

    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    # TODO
    numPatient=300
    tsList=[0,75,150,300]
    postStep=150
    for preSteps in tsList:
        finalPop=[]
        print('Histogram plotting for preSteps {0}'.format(preSteps))
        totPopList,resistPopList=performSim(numPatient,
                                          preSteps,postStep)
        for i in totPopList:
            finalPop.append(i[-1])
        Xlabel='filan total virus population'
        Ylabel='number of patients'
        Title='Distribution of final total \population corresponding to {0} patients and {1} preSteps'\
        .format(numPatient,preSteps)
        pylab.figure()
        pylab.hist(finalPop,12)
        pylab.xticks(range(0,650,50),['0','50','100','150','200'\
                     ,'250','300','350','400','450','500','550','600'])
        pylab.ylabel(Ylabel)
        pylab.xlabel(Xlabel)
        pylab.title(Title)
        print('Histogram plotting done for preSteps {0}'.format(preSteps))

def testProblem5():
    sTime=time.time()
    problem5()
    eTime=time.time()
    totTime=eTime-sTime
    print('time using: ',totTime)

#testProblem5()
#
# PROBLEM 6
#

def performSim6(numPatient,preGutt,mid,postGrim):
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO
    # create two list of list to record the population in every timestep in every simulations
    totPopList,resistPopList=[],[]
    maxBirthProb,clearProb,resistances,mutProb=0.1,0.05,{'guttagonol':False,'grimpex':False},0.005
    numViruses,maxPop=100,1000
    for j in range(numPatient):
        
        # reset a list of resistant viruses in every trial simulation
        viruses=[]
        for k in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb,clearProb,resistances,mutProb))
        patient=Patient(viruses,maxPop)
        totPop,resistPop=[],[]  # reset two list to record pop in every simulation
        
        # simulate over timesteps
        for step in range(preGutt+mid+postGrim):
            if step==preGutt:
##                print(patient.getPrescriptions())
                patient.addPrescription('guttagonol')
##                print(patient.getPrescriptions())
            elif step==(preGutt+mid):patient.addPrescription('grimpex')
            totPop.append(patient.getTotalPop())
            resistPop.append(patient.getResistPop(['guttagonol','grimpex']))
            patient.update(step)
        totPopList.append(totPop)
        resistPopList.append(resistPop)
    return totPopList,resistPopList

def problem6():
    """
    Runs simulations and make histograms for problem 6.

    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
    
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    # TODO
    numPatient=300 
    preGutt,midList,postGrim=150,list(reversed([0,75,150,300])),150
    for mid in midList:
        finalPop=[]
        print('Histogram plotting for middle timesteps {0}'.format(mid))
        totPopList,resistPopList=performSim6(numPatient,
                                             preGutt,mid,postGrim)
        for i in totPopList:
            finalPop.append(i[-1])
        Xlabel='filan total virus population'
        Ylabel='number of patients'
        Title='Distribution of final total population with two drugs\ncorresponding to {0} patients and {1} middle timesteps'\
        .format(numPatient,mid)
        pylab.figure()
        pylab.hist(finalPop,12)
        pylab.xticks(range(0,650,50),['0','50','100','150','200'\
                     ,'250','300','350','400','450','500','550','600'])
        pylab.ylabel(Ylabel)
        pylab.xlabel(Xlabel)
        pylab.title(Title)
        print('Histogram plotting done for middle timesteps {0}'.format(mid))

def testProblem6():
    sTime=time.time()
    problem6()
    eTime=time.time()
    totTime=eTime-sTime
    print('time using: ',totTime)

#testProblem6()
#
# PROBLEM 7
#
 
def performSim7(numTrials,preGutt,mid,postGrim):
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO
    # create two list of list to record the population in every timestep in every simulations
    totPopList,gutPopList,grimPopList,bothPopList=[],[],[],[]
    maxBirthProb,clearProb,resistances,mutProb=0.1,0.05,{'guttagonol':False,'grimpex':False},0.005
    numViruses,maxPop=100,1000
    for j in range(numTrials):
        
        # reset a list of resistant viruses in every trial simulation
        viruses=[]
        for k in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb,clearProb,resistances,mutProb))
        patient=Patient(viruses,maxPop)
        totPop,gutPop,grimPop,bothPop=[],[],[],[]  # reset two list to record pop in every simulation
        
        # simulate over timesteps
        for step in range(preGutt+mid+postGrim):
            if step==preGutt:
##                print(patient.getPrescriptions())
                patient.addPrescription('guttagonol')
                patient.addPrescription('grimpex')
##                print(patient.getPrescriptions())
            elif step==(preGutt+mid):patient.addPrescription('grimpex')
            totPop.append(patient.getTotalPop())
            gutPop.append(patient.getResistPop(['guttagonol']))
            grimPop.append(patient.getResistPop(['grimpex']))
            bothPop.append(patient.getResistPop(['guttagonol','grimpex']))
            patient.update(step)    # the argument step is used to test
        totPopList.append(totPop)
        gutPopList.append(gutPop)        
        grimPopList.append(grimPop)
        bothPopList.append(bothPop)
    return totPopList,gutPopList,grimPopList,bothPopList

def Plot7(Ydata,Xlabel,Ylabel,Title,Legend=None):
    pylab.plot(Ydata, label=Legend)
    # Place a legend to the right of this smaller subplot.
    pylab.legend()
    # Place a legend above this subplot, expanding itself to
    # fully use the given bounding box.
#    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#               ncol=2, mode="expand", borderaxespad=0.)
    pylab.ylabel(Ylabel)
    pylab.xlabel(Xlabel)
    pylab.title(Title)

def problem7():
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.

    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        
    """
    # TODO
    numTrials=10
    preGutt,midList,postGrim=150,list(reversed([0])),850
    for mid in midList:
        finalPop=[]
#        print('Histogram plotting for middle timesteps {0}'.format(mid))
        totPopList,gutPopList,grimPopList,bothPopList=performSim7(numTrials,preGutt,mid,postGrim)
    totPop=computeMeans(totPopList)
    gutPop=computeMeans(gutPopList)
    grimPop=computeMeans(grimPopList)
    bothPop=computeMeans(bothPopList)
    Xlabel='time'
    Ylabel='population'
    Title='population dynamics with two drugs'
    totLegend='Total'
    gutLegend='Guttagono'
    grimLegend='Grimpex'
    bothLegend='Both'
    pylab.figure()
    Plot7(totPop,Xlabel,Ylabel,Title,totLegend)
    Plot7(gutPop,Xlabel,Ylabel,Title,gutLegend)
    Plot7(grimPop,Xlabel,Ylabel,Title,grimLegend)
    Plot7(bothPop,Xlabel,Ylabel,Title,bothLegend)
    
def testProblem7():
    sTime=time.time()
    problem7()
    eTime=time.time()
    totTime=eTime-sTime
    print('time using: ',totTime)

#testProblem7()
    