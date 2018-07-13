"""Equation |"""
from math import log10
def main():
    """Main function"""
    num = float(input())
    equa = 2*log10(num) + (num/3)
    print("%.2f"% equa)
main()

