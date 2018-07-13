"""Number Digit"""
def main():
    """Main function"""
    amount = str(abs(int(input())))
    num = int(input())

    if num > len(amount):
        print("Index out of range.")
    elif num <= 0:
        print("Index error.")
    else:
        print(amount[-num])
main()



