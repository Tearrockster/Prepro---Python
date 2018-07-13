"""Please Ask Me"""
def main():
    """Main function"""
    people = int(input())
    if people >= 8:
        print("Extremely Happy")
    elif people >= 4:
        print("Very Happy")
    elif people >= 1:
        print("Happy")
    else:
        print("Sad")
main()
