"""Which Case?"""
def main():
    """Main function"""
    sentence = input()

    if sentence.isupper():
        print("This sentence is written in uppercase.")
    elif sentence.islower():
        print("This sentence is written in lowercase.")
    else:
        print("This sentence is written in both uppercase and lowercase.")
main()
