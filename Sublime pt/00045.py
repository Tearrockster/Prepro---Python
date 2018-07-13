"""BTS Skytrain EP.2"""
def main():
    """Main function"""
    time = int(input())
    if time > 120:
        print("Exceed, You will be fined!")
    if time <= 120:
        print("No, You are safe!")
main()
