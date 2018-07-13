"""Password Restriction EP.1"""
def main():
    """Main function"""
    password = input()

    if password.isalpha():
        print("You can use this Password")
    else:
        print("You can't use this Password")
main()
