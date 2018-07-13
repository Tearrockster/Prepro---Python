"""[Extra] Cryptography EP.2 - Caesar Out"""
def main():
    """Main function"""
    char = ord(input())
    if 88 <= char <= 90:
        char -= 23
        print(chr(char))
    elif 65 <= char <= 87:
        char += 3
        print(chr(char))
    elif 97 <= char <= 119:
        char += 3
        print(chr(char))
    elif 120 <= char <= 122:
        char -= 23
        print(chr(char))
    else:
        print(chr(char))

main()
