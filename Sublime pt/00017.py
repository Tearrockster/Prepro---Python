"""Middle Value"""
def main():
    """Main function"""
    price1 = int(input())
    price2 = int(input())
    price3 = int(input())
    check1 = max(price1, price2, price3)
    check2 = min(price1, price2, price3)
    alt = price1 + price2 + price3
    equa = alt - check1 - check2
    print(equa)
main()



