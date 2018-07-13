"""Summation"""
def main():
    """Main function"""
    amount = int(input())
    total = 0

    for _ in range(amount):
        realnum = float(input())
        total += float(input())
        print("%.4f" % total)
main()
