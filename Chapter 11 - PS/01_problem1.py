class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")
        

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
i=int(input(f"Enter 2D vector i:- ")) 
j=int(input(f"Enter 2D vector j:- ")) 
a = TwoDVector(i,j) 
a.show()
i = int(input("Enter 3D vector i component: "))
j = int(input("Enter 3D vector j component: "))
k = int(input("Enter 3D vector k component: "))
b = ThreeDVector(i,j,k)
b.show()
