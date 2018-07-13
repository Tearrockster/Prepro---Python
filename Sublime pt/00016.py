"""Introduction to Calculus"""
from math import sin, cos
def main():
    """Main function"""
    num1 = int(input())
    num2 = int(input())
    numb = max(num1, num2)
    numa = min(num1, num2)
    equa = (-3/2*cos(2*numb/3) - sin(numb) + (4*numb)) - (-3/2*cos(2*numa/3) - sin(numa) + (4*numa))
    print("%.2f"% equa)
main()


