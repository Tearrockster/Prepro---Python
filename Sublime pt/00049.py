"""Password Validation"""
def main():
    """Main function"""
    password = input()
    amount = len(password)
    if amount >= 8:
        print("Password is valid, you can use this password.")
    if amount < 8:
        print("Password too short, try again.")
main()
