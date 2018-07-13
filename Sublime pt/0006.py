"""Election Chance"""
def main():
    """Main function"""
    chance = int(input())
    year = int(input())
    elec = 1 - (chance/100*(year-2018))
    chance2 = 0 <= elec <= 1
    result = (elec*100) * chance2

    print(int(result), "%")


main()


