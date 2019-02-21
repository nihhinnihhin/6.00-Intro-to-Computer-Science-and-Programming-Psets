    # Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:
# ??? global variable and the definition of POS

import math
import random
import pylab
import ps11_visualize

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.    
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)
    def __eq__(self,other):
        return self.x==other.getX() and self.y ==other.getY()


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
   
    decision: 2D plane.
    (Maybe the term "constraint"  would be more suitable in theoretical machanics)
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # TODO: Your code goes here
        self.width=int(width)
        self.height=int(height)
        self.cleanedTiles=[]
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # TODO: Your code goes here
        # mistake: forget to convert the x,y coordinates, so there a lot
        # duplicate in the Cleaned Tiles list
        if  (int(pos.getX()),int(pos.getY())) not in self.cleanedTiles:
            self.cleanedTiles.append((int(pos.getX()),int(pos.getY())))
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # TODO: Your code goes here
        return (m,n) in self.cleanedTiles
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return self.width*self.height
    def getCleanedTiles(self):
        return self.cleanedTiles
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return len(self.cleanedTiles)
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # TODO: Your code goes here
        return Position(self.width*random.random(),self.height*random.random())
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        # TODO: Your code goes here
        return 0<=pos.getX()<=self.width and 0<=pos.getY()<=self.height

#room=RectangularRoom(1,2)
#room.getRandomPosition()
class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # TODO: Your code goes here
        self.room=room
        self.speed=float(speed)
        self.d=random.randrange(0,360)
        self.p=self.room.getRandomPosition()
#    def getRobotRoom(self):
#        '''
#        Return the room the robot cleaning
#        
#        Returns: a room object giving the room the robot cleaning
#        '''
#        return 
#    def getRobotSpeed(self):
#        """
#        return the speed of the robot
#        
#        returns: a float giving the speed of the robot
#        """
#        return self.speed
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        # TODO: Your code goes here
        return self.p
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # TODO: Your code goes here
        return self.d
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        # TODO: Your code goes here
        self.p=position
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        # TODO: Your code goes here
        self.d=direction
        


class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here
        oldPos=self.getRobotPosition()
        newPos=oldPos.getNewPosition(self.getRobotDirection(),self.speed)
        # in the method of a class or a subclass inherited from superclass, 
        # there is no data hiding, i.e. the reference of variable could be 
        # directly self.speed, self.x, etc.
        # hits a wall?
        if not self.room.isPositionInRoom(newPos):
            self.setRobotDirection(random.randrange(0,360))
        else:
            self.room.cleanTileAtPosition(newPos)
            self.setRobotPosition(newPos)


# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize=True):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    
    # TODO: Your code goes her
    covsList=[]
    timeList=[]
    for i in range(num_trials):
#        anim=ps11_visualize.RobotVisualization(num_robots,width,height)
        # inner loop is below
        coverages=[0]
        timeSteps=0
        room=RectangularRoom(width,height)
        Robots=[]
        for i in range(num_robots):
            Robots.append(robot_type(room,speed))
        while coverages[-1]<min_coverage:
#            anim.update(room,Robots)
            for i in range(num_robots):
                Robots[i].updatePositionAndClean()
                coverage=room.getNumCleanedTiles()/room.getNumTiles()
                coverages.append(coverage)
            timeSteps+=1
    #        print('coverage: {0:.2f}\tPos: ({1:.1f},{2:.1f})'.format(coverage,Robot.getRobotPosition().getX(),Robot.getRobotPosition().getY()))
    #        print('cleanedTiles:',room.getCleanedTiles())
        timeList.append(timeSteps)
#        print('total steps',timeSteps)
        covsList.append(coverages)
#        anim.done()
    return covsList,timeList
def test():
    num_robots=100
    speed=1
    width=10
    height=10
    min_coverage=1
    num_trials=2
    robot_type=RandomWalkRobot
    visualize=True
    L_of_L=runSimulation(num_robots,speed,width,height,min_coverage,num_trials,robot_type,visualize)

def testHelper():
    test()

#TilesSet=set(Tiles)
#print('no repeated: ',len(TilesSet),' original:',len(Tiles))
#print(TilesSet,'\n',Tiles)

# === Provided function
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


# === Problem 4
def showPlot1(robot_type):
    """
    Produces a plot showing dependence of cleaning time on room size.
    
    Y-axis: the mean time over numTrials
    X-axis: the room size
    """
    # TODO: Your code goes here
    meanTimes=[]
    roomSizes=list(range(5,30,5))
    num_robots=1
    speed=1
    min_coverage=0.75
    num_trials=10
    visualize=True
    for i in roomSizes:
        width=i
        height=i
        covsList,timeList=runSimulation(num_robots,speed,width,height,\
                                        min_coverage,num_trials,robot_type,visualize)
        meanTimes.append(sum(timeList)/len(timeList))
#    print(meanTimes,roomSizes)
    pylab.figure()
    pylab.plot(roomSizes,meanTimes)
#    pylab.axis([0,30,0,4000])
    pylab.ylabel('Timesteps over {0} times simulation'.format(num_trials))
    pylab.xlabel('room size over 5*5 to 25*25')
    pylab.title('Time to clean 75% of a square room with 1 robot, for various room sizes')
    
def showPlot2(robot_type):
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here
    meanTimes=[]
    numRoList=list(range(1,11))
    width=25
    height=25
    speed=1
    min_coverage=0.75
    num_trials=10
    visualize=True
    for i in numRoList:
        num_robots=i
        covsList,timeList=runSimulation(num_robots,speed,width,height,\
                                        min_coverage,num_trials,robot_type,visualize)
        meanTimes.append(sum(timeList)/len(timeList))
#    print(numRoList,meanTimes)
    pylab.figure()
    pylab.plot(numRoList,meanTimes)
#    pylab.axis([0,30,0,4000])
    pylab.ylabel('Timesteps over {0} times simulation'.format(num_trials))
    pylab.xlabel('number of robots')
    pylab.title('TIme to clean 75% of a 25*25 square room with different robots')
def showPlot3(robot_type):
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here
    meanTimes=[]
    roomDs=[(20,20),(25,16),(40,10),(50,8),(80,5),(100,4)]
    roomRatio=[]
    speed=1
    min_coverage=0.75
    num_trials=10
    visualize=True
    num_robots=2
    for i in roomDs:
        width=i[0]
        height=i[1]
        roomRatio.append(width/height)
        covsList,timeList=runSimulation(num_robots,speed,width,height,\
                                        min_coverage,num_trials,robot_type,visualize)
        meanTimes.append(sum(timeList)/len(timeList))
#    print(numRoList,meanTimes)
    pylab.figure()
    pylab.plot(roomRatio,meanTimes)
#    pylab.axis([0,30,0,4000])
    pylab.ylabel('Timesteps over {0} times simulation'.format(num_trials))
    pylab.xlabel('the ratio width/height of room in the same size')
    pylab.title('Time to clean 75% of a room in the same size with 2 robots for various room dimensions: ratio of width to height')
def showPlot4(robot_type):
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here
    speed=1
    num_trials=10
    visualize=True
    percentages=arange(10,110,10)/100
#    percentages=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    width=25
    height=25
    pylab.figure()
#    for i in numRoList:
#    print(i)
    for i in range(1,6):
        meanTimes=[]
#        print(i)
        num_robots=i
        for j in percentages:
            min_coverage=j
            covsList,timeList=runSimulation(num_robots,speed,width,height,\
                                            min_coverage,num_trials,robot_type,visualize)
            meanTimes.append(sum(timeList)/len(timeList))
#        print(len(percentages),len(meanTimes))
        line, = pylab.plot(percentages,meanTimes, label='robots number:{0}'.format(i))
        pylab.legend()
    #    pylab.axis([0,30,0,4000])
        pylab.ylabel('Timesteps over {0} times simulation'.format(num_trials))
        pylab.xlabel('minimum coverage')
        pylab.title('Time to clean different percentage of room, for various robots')

# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # TODO: Your code goes here
    def updatePositionAndClean(self):
        oldPos=self.getRobotPosition()
        newPos=oldPos.getNewPosition(self.getRobotDirection(),self.speed)
        # hits a wall?
        if not self.room.isPositionInRoom(newPos):
            self.setRobotDirection(random.randrange(0,360))
        # 
        else:
            self.room.cleanTileAtPosition(newPos)
            self.setRobotPosition(newPos)
            self.setRobotDirection(random.randrange(0,360))

showPlot4(Robot)

# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    and works together 
    
    from the data, obviously, the efficiency of randomWalk robot is
    several times to the standard typeo
    """
    # TODO: Your code goes here
    showPlot1(RandomWalkRobot)
    showPlot1(Robot)
    showPlot2(RandomWalkRobot)
    showPlot2(Robot)
    showPlot3(RandomWalkRobot)
    showPlot3(Robot)
    showPlot4(RandomWalkRobot)
    showPlot4(Robot)
def compareAndExplore(robot_type):
    showPlot5()   
