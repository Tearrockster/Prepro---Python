"""Equation ||"""
from math import radians, sin, fabs
def main():
    """Main function"""
    num = int(input())
    equa = sin(3*radians(num)) + fabs(num/4) + 5
    print("%.2f" %equa)
main()

