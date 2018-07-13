"""Leap Year"""
def main():
    """Main function"""
    year = int(input())
    if year%4 == 0 and year%100 > 0 or year%400 == 0 and year >= 0:
        print("%d is leap year."%year)
    elif year < 0:
        print("This year does not exist.")
    else:
        print("%d is not leap year."%year)
main()

