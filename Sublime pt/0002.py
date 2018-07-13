"""Percentage"""
def main():
    """Main function"""
    mny = int(input())
    allmny = int(input())
    name = input()
    percen = (mny * 100)/allmny
    print("%s %.2f%%" %(name, percen))
main()


