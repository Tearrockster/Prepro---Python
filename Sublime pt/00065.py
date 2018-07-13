"""Month Days Advanced"""
def main():
    """Main function"""
    function()



def function():
    """My function"""
    month = int(input())
    year = int(input())
    if month in (1, 3, 5, 7, 8, 10, 12):
        print("31")
    elif month in (4, 6, 9, 11):
        print("30")
    elif month > 12 or month <= 0 or year <= 0:
        print("Invalid Month or Year")
    elif month == 2:
        if year%4 == 0 and year%100 > 0 or year%400 == 0 and year >= 0:
            print("29")
        else:
            print("28")
main()


