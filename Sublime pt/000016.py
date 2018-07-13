"""First and Last"""
def main():
    """Main function"""
    text = input()

    check = (text[-1])
    check1 = text[0]
    if check1 == check:
        print("Yes")
    if check1 != check:
        print("No")
main()
