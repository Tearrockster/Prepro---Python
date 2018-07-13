"""Where is O"""
def main():
    """Main function"""
    text = input().upper()
    target = text.find('O')

    if text.find('O') >= 0:
        new = target + 1
        print("O is at %d"%new)
    else:
        print("There is no O here")
main()
