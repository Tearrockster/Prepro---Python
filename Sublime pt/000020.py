"""Palindrome"""
def main():
    """Main function"""
    text = input()
    if text == text[::-1]:
        print("Yes")
    if text != text[::-1]:
        print("No")
main()
