"""Month Days Advanced"""
def main():
    """Main function"""
    month = int(input())
    year = int(input())





def function():
    """My function"""
    if month == 12 or month == 1 or month == 3 or month == 5:
        print("31")
    elif month == 7 or month == 8 or month == 10 or month == 12:
        print("31")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30")
    elif month > 12 or month <= 0 :
        print("Invalid Month or Year")
    elif year == 2 and year%4 == 0 and year%100 > 0 or year%400 == 0 and year >= 543:
        print("29")

