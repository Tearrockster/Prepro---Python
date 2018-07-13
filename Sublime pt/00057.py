"""Basic Split Function"""
def main():
    """Main function"""
    num1 = float(input())
    if num1 < 0:
        equa1 = (num1**2)
        print("%.2f"%equa1)
    if num1 == 0:
        print("0.00")
    if num1 > 0:
        equa2 = ((2 * num1) + 10)
        print("%.2f"%equa2)
main()

