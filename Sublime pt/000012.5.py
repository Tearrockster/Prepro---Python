"""[Extra] Cryptography EP.3 - Caesar N Cipher"""
def main():
    """Main function"""
    num = int(input())
    alphabet = ord(input())
    if 65 <= alphabet <= 67 and num > 0:
        alphabet -= num
        print(chr(alphabet))
    if 68 <= alphabet <= 90 and num > 0:
        alphabet -= num
        print(chr(alphabet))
    if 97 <= alphabet <= 99 and num > 0:
        print(chr(alphabet))
    if 100 <= alphabet <= 122 and num > 0:
        print(chr(alphabet))
    
