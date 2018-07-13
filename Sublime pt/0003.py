"""Energy"""
def main():
    """Main function"""
    distance = float(input())
    energy = int(input())
    ener = distance * 1000/10
    amount = ener//energy + int(ener%energy > 0)
    print(int(amount))
main()
