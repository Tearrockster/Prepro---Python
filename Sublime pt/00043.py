"""Normal If Conditional Problem"""
def main():
    """Main function"""
    num1 = int(input())

    if num1 %2 != 0:
        print("This is an odd number.")
    elif num1 %2 == 0:
        print("This is an even number.")
main()
