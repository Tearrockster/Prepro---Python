"""[Extra] Cryptography EP.1 - Caesar In"""
def main():
    """Main function"""
    char = ord(input())
    if 65 <= char <= 67:
        char += 23
        print(chr(char))
    elif 68 <= char <= 90:
        char -= 3
        print(chr(char))
    elif 97 <= char <= 99:
        char += 23
        print(chr(char))
    elif 100 <= char <= 122:
        char -= 3
        print(chr(char))
    else:
        print(chr(char))

main()
