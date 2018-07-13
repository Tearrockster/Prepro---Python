"""Pancake Shop EP.5"""
def main():
    """Main function"""
    num = float(input())
    print("|--------|")
    print("|%-8.2f|"%num)
    print("|--------|\n")

    print("|--------|")
    print("|%8.2f|"%num)
    print("|--------|\n")

    print("|--------|")
    print("|%08.2f|"%num)
    print("|--------|")
main()
