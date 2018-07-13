"""Month Days 2018"""
def main():
    """Main function"""
    function()





def function():
    """My function"""
    month = int(input())
    if month == 12 or month == 1 or month == 3 or month == 5:
        print("31")
    elif month == 7 or month == 8 or month == 10 or month == 12:
        print("31")
    if month == 4 or month == 6 or month == 9 or month == 11:
        print("30")
    if month > 12 or month <= 0:
        print("Invalid Month")
    if month == 2:
        print("28")
main()
