class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=int(input(" length of rectangle: "))
b=int(input(" breadth of rectangle: "))
obj=rectangle(a,b)
print("area of rectangle:",obj.area())
 
print()
