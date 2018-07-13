"""Shorten"""
def main():
    """Main function"""
    text = input()
    check = len(text)
    if check < 3:
        print(text)
    if check >= 3:
        print(text[:3:])
main()
