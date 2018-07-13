"""Four Dots"""
from math import (sqrt)
def main():
    """Main function"""
    xa1 = int(input())
    ya1 = int(input())
    xb1 = int(input())
    yb1 = int(input())
    xc1 = int(input())
    yc1 = int(input())
    xd1 = int(input())
    yd1 = int(input())

    space1 = (function(xb1, xa1, yb1, ya1))
    space2 = (function(xc1, xb1, yc1, yb1))
    space3 = (function(xd1, xc1, yd1, yc1))
    space4 = (function(xd1, xa1, yd1, ya1))
    allspace = space1 + space2 + space3 + space4



    print("%.2f"%allspace)

def function(x22, x11, y22, y11):
    """My Function"""

    space = sqrt((x22 - x11)**2 + (y22 - y11)**2)#equa find d
    return space

main()





