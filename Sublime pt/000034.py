"""Grade A"""
def main():
    """Main function"""
    grade = input()
    equa = grade.count('A')

    if "A" in grade:
        print(equa)
    else:
        print("Oops")
main()
