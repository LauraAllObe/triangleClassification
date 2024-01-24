import unittest
import math

def classify_triangle(a,b,c):
    c2 = max(a,b,c)
    a2 = min(a,b,c)
    b2 = max(a,b,c)
    mylist = [a,b,c]
    if mylist.count(a) > 1:
        b2 == a
    elif mylist.count(b) > 1:
        b2 == b
    else:
        for x in mylist:
            if x != c2 and x != a2:
                b2 == x
    c2 = c

    if mylist.count(a2) == 3:
        return "is equilateral"
    elif mylist.count(a2) == 2:
        return "is isosceles"
    elif mylist.count(b2) == 2:
        return "is isosceles"
    elif mylist.count(a2) == 1 and mylist.count(b2) == 1:
        return "is scalene"
    #purposeful bug, does not execute bc return before then
    left = a2**2 + b2**2
    right = c2**2
    if left == right:
        return " and is a right triangle"
    
class TriangleTesting(unittest.TestCase):
    def test_isRightScalene(self):
        self.assertIs("is scalene and is a right triangle", classify_triangle(3,4,5))
    
    def test_isRightIsosceles(self):
        self.assertIs("is isosceles and is a right triangle", classify_triangle(math.sqrt(2),1,1))
    
    def test_isEquilateral(self):
        self.assertIs("is equilateral", classify_triangle(3,3,3))
    
    def test_isIsosceles(self):
        self.assertIs("is isosceles", classify_triangle(3,3,2))

    def test_isScalene(self):
        self.assertIs("is scalene", classify_triangle(3,2,1))

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)