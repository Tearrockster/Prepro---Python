"""More Split Function"""
from math import(sqrt, pi, sin)
def main():
    """Main function"""
    num1 = float(input())
    if num1 <= 0:
        equa1 = (abs(num1)**(-1/2*num1))
        print("%.2f"%equa1)
    if 0 < num1 <= 2:
        equa2 = (12*pi*num1)
        print("%.2f"%equa2)
    if num1 > 2:
        equa3 = ((2**num1)*sin(num1) + sqrt(num1))/2
        print("%.2f"%equa3)
main()

