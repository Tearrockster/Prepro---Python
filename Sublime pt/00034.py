"""Name List"""
def main():
    """Main function"""
    start = int(input())
    name(start, 0)
    name(start, 1)
    name(start, 2)
    name(start, 3)
    name(start, 4)
    name(start, 5)
    name(start, 6)
    name(start, 7)
    name(start, 8)
    name(start, 9)

def name(num, num_1):
    """Function"""
    name1, name2 = input(), input()
    name3, name4 = input(), input()
    name5 = input()

    print("ID#%d\t%s" %((num + 5*num_1), name1))
    print("ID#%d\t%s" %((num + 5*num_1+1), name2))
    print("ID#%d\t%s" %((num + 5*num_1+2), name3))
    print("ID#%d\t%s" %((num + 5*num_1+3), name4))
    print("ID#%d\t%s" %((num + 5*num_1+4), name5))
main()
