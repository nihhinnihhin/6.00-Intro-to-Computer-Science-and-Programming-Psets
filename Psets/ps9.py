# 6.00 Problem Set 9
#
# Name:
# Collaborators:Internet
# Time:(start:9:15)
# ???: why area method doesn't have double underscore

filename='shapes.txt'

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")


class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):
    def __init__(self,b,h):
        '''
        b: base of the Triangle
        h: height of the Triangle
        '''
        self.base=float(b)
        self.height=float(h)
    def area(self):
        '''
        returns area the Triangle
        '''
        return 0.5*self.base*self.height
    def __str__(self):
        return 'Triangle with base {0} and height {1}'\
    .format(self.base,self.height)
    def __eq__(self,other):
        '''
        Two Triangle are equal if they have the same base and height
        other: object to check for equality
        '''
        return type(other)==Triangle and self.base==other.base and\
    self.height==other.height

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.members=[]
        self.index=0    #???
#        self.set=set()  # create an empty set
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
#        if sh not in self.set:
#            self.set.add(sh)
        if sh not in self.members:
            self.members.append(sh)
        # after every addition operation, categorize the shapeset
        # TO DO
        
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
#        for i in self.set:
#            yield i
        for i in self.members:
            yield i
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        whole_string=''
        for i in self.members:
            if type(i)==Circle:
                whole_string+=i.__str__()+'\n'
        for i in self.members:
            if type(i)==Square:
                whole_string+=i.__str__()+'\n'
        for i in self.members:
            if type(i)==Triangle:
                whole_string+=i.__str__()+'\n'
        return whole_string
#        for i in self.set:
#            whole_string+=i.__str__()+'\n'
#        return whole_string
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    Largests=(0,)
    for each in shapes.members:
        try:
            if each.area()>Largests[0].area():
                Largests=(each,)
            elif each.area()==Largests[0].area(): Largests+=(each,)
        except AttributeError:
            Largests=(each,)
    return Largests
#    maxShape=Triangle(0,0)
#    Largest=()
#    for i in shapes.set:            # find the largest one
#        if i.area()>=maxShape.area():
#            maxShape=i
#    for i in shapes.set:             # add all the items with 
#        if maxShape.area()==i.area():   # the same larest area in a tuple
#            Largest+=(i,)
            
#%%
def test_class_Shape():
    ss=ShapeSet()
    ss.addShape(Triangle(1.2,2.5))
    ss.addShape(Circle(4))
    ss.addShape(Square(3.6))
    ss.addShape(Triangle(1.6,6.4))
    ss.addShape(Circle(2.2))
    Largest=findLargest(ss)
    Largest
    for e in Largest: print(e)
    
    ss = ShapeSet()
    ss.addShape(Triangle(3,8))
    ss.addShape(Circle(1))
    ss.addShape(Triangle(4,6))
    Largest = findLargest(ss)
#    Largest
    for e in Largest:print(e)
    Largest
    
    t=Triangle(3,8)
    t==Largest[0]   # >>>True
    t is Largest[0] # >>>Farlse
    id(Largest[0]),id(t)    
    # >>>(2026116289144, 2026116070648)
    # conclusion: 'is' is shallow equality;
    # '==' is deep equality due to method __eq__
    
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    ss=ShapeSet()
    inputFile=open(filename)
    for line in inputFile:
        line_copy=line.strip('\n')
        shape=line_copy.split(',')
        if shape[0]=='triangle':
            ss.addShape(Triangle(float(shape[1]),float(shape[2])))
        elif shape[0]=='square':
            ss.addShape(Square(float(shape[1])))
        elif shape[0]=='circle':
            ss.addShape(Circle(float(shape[1])))
    return ss
        
def test_read():
    ss=readShapesFromFile('shapes.txt')
    print(ss)

#test_read()
