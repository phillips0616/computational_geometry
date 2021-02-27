#Given two points, p1 and p2, check if p1 is clockwise from p2 with respect from the origin.
#this uses the cross product of 2d vectors and the fact that the sign of the result of that product
#will tell us whether p1 is clockwise from p2 or not.
#this algorithm comes from the computational geometry section of CLRS.

#class to define the concept of point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def compute_xproduct(p1, p2):
    return p1.x*p2.y - p2.x*p1.y

#returns true if clockwise, otherwise false
def clockwise(p1,p2):
    return compute_xproduct(p1, p2) > 0

p1 = Point(2,3)
p2 = Point(3,1)

print(clockwise(p1,p2))

p1 = Point(-5,2)
p2 = Point(-4,-2)

print(clockwise(p1,p2))