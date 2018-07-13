"""Condition Mod"""
def main():
    """Main function"""
    num1 = int(input())
    if num1%2 > 0:
        print("Oooo")
    elif num1%2 == 0 and 2 <= num1 <= 5:
        print("lelelel")
    elif num1%2 == 0 and 6 <= num1 <= 20:
        print("OMG!")
    elif num1%2 == 0 and num1 > 20:
        print("Infinite!")
    else:
        print("Out of condition!")
main()
