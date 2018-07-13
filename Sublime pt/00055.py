"""Grade"""
def main():
    """Main function"""
    grade = int(input())
    if 0 <= grade <= 49:
        print("0")
    elif 50 <= grade <= 54:
        print("1")
    elif 55 <= grade <= 59:
        print("1.5")
    elif 60 <= grade <= 64:
        print("2")
    elif 65 <= grade <= 69:
        print("2.5")
    elif 70 <= grade <= 74:
        print("3")
    elif 75 <= grade <= 79:
        print("3.5")
    elif 80 <= grade <= 100:
        print("4")
    else:
        print("invalid")
main()
