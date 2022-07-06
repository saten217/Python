##class Polygon:
##    def __init__(self, no_of_sides):
##        self.n = no_of_sides
##        self.sides = [0 for i in range(no_of_sides)]
##
##    def inputSides(self):
##        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
##
##    def dispSides(self):
##        for i in range(self.n):
##            print("Side",i+1,"is",self.sides[i])
##
##
##class Triangle(Polygon):
##    def __init__(self):
##        Polygon.__init__(self,3)
##
##    def findArea(self):
##        a, b, c = self.sides
##        # calculate the semi-perimeter
##        s = (a + b + c) / 2
##        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
##        print('The area of the triangle is %0.2f' %area)
##
##class Square(Polygon):
##    def __init__(self):
##        Polygon.__init__(self,1)
##
##    def findArea(self):
##        a= self.sides
##        # calculate the semi-perimeter
##        area= a[0]**2
##        #area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
##        print('The area of the triangle is %0.2f' %area)
##
##class Circle(Polygon):
##    def __init__(self):
##        Polygon.__init__(self,1)
##
##    def findArea(self):
##        a= self.sides
##        # calculate the semi-perimeter
##        area= (a[0]**2)*3.14
##        #area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
##        print('The area of the circle is %0.2f' %area)
##        
###t= Square()       
###t = Triangle()
##t=Circle()
##t.inputSides()
##t.dispSides()
##t.findArea()



#part 2
##class Robot(object):
##   def __init__(self):
##      self.a = 123
##      self._b = 345
##      self.__c = 678
##
##obj = Robot()
##print(obj.a)
##print(obj._b)
##print(obj.__c)

###part 3
##class Robot(object):
##   def __init__(self):
##      self.__version = 22
##
##   def getVersion(self):
##      print(self.__version)
##      return self.__version
##
##   def setVersion(self, version):
##      self.__version = version
##
##obj = Robot()
##obj.getVersion()
##obj.__version =34 
#####print("updated",obj.getVersion())
##obj.setVersion(32222)
##obj.getVersion()
##a=obj.getVersion()
##print("Value of the updated version", a)
##

#part 4

class Car:

    def __init__(self):
        self.__updateSoftware()
    def update(self):
        self.__updateSoftware()

    def drive(self):
        print ('driving')

    def __updateSoftware(self):
        print ('updating software')
redcar = Car()
redcar.drive()
redcar.update()  #not accesible from object.





















