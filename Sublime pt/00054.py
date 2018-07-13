"""Health Record"""
def main():
    """Main function"""
    function(1)
    function(2)
    function(3)
    function(4)
    function(5)


def function(num):
    """My function"""
    name = input()
    birth = int(input())
    month = int(input())
    year = int(input())
    print("** Patient No.%d **" %num)
    print("Full name: %s" %name)
    print("Birthday: %d/%d/%d\n" %(birth, month, year))
main()
