"""Password Restriction EP.2"""
def main():
    """Main function"""
    password = input()
    if password.isnumeric():
        print("You can use this Password")
    else:
        print("You can't use this Password")
main()
