"""Pancake Shop EP.3"""
def main():
    """Main function"""
    text = input()
    equa = 20 - len(text)
    equa1 = ' ' * (equa//2)
    equa2 = ' ' * (equa % 2 > 0)



    print("|--------------------|")
    print("|%s%s%s|"%(equa1, text, equa1 + equa2))
    print("|--------------------|")


main()
