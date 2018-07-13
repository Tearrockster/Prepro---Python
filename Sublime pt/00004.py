"""Alphabet Sequence"""
def main():
    """Main function"""
    alphabet = input()
    for i in range(ord('A'), ord('Z') + 1):
        if chr(i) > alphabet:
            break
        print(chr(i), end='')
        if chr(i) <= alphabet:
            break
        print(chr(i), end='')
main()
