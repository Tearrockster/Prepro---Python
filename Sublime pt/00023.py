"""Black Canyon"""
def main():
    """Main function"""
    price1 = myfunction(int(input()), int(input()))
    price2 = myfunction(int(input()), int(input()))
    price3 = myfunction(int(input()), int(input()))
    price4 = myfunction(int(input()), int(input()))
    price5 = myfunction(int(input()), int(input()))
    total = price1 + price2 + price3 + price4 + price5
    result = total * 10/100
    alt = total - result
    print("Total : %.2f Baht" % alt)




def myfunction(cake, drink):#x = price cake, y = price drink
    """Myfunction"""

    equa = (cake + drink)*20/100
    equa1 = (cake + drink) - equa
    return equa1

main()

