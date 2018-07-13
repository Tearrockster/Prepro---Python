"""Good Afternoon"""
def main():
    """Main function"""
    hour = int(input())
    minute = int(input())
    if 5 <= hour <= 11 and 0 <= minute <= 59:
        print("Good Morning")
    if 12 <= hour <= 17 and 0 <= minute <= 59:
        print("Good Afternoon")
    if 18 <= hour <= 22 and 0 <= minute <= 59:
        print("Good Evening")
    if 0 <= hour <= 4 or hour == 23 and 0 <= minute <= 59:
        print("Good Night")
main()
