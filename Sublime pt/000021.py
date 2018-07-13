"""Dog Tag"""
def main():
    """Main function"""
    name = input()
    name1 = 8 - len(name)
    equa = ' ' * (name1//2)
    equa1 = ' ' * (name1%2 > 0)

    print("/--------\\")
    print("|%s%.8s%s|"%(equa, name, equa + equa1))
    print("\\--------/")

main()
