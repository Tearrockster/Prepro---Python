"""Pancake"""
def main():
    """Main function"""
    amount = int(input())
    extra = int(input())
    demand = int(input())
    pack = amount + extra   #Pack size

    pay, get = 0, 0
    while demand >= pack:
        #Recieve one pack of pancake
        get += pack
        pay += amount*20
        demand -= pack

    if demand < amount:
        get += demand
        pay += demand*20

    elif demand >= amount:
        get += pack
        pay += amount*20

    print('Pay:', pay)
    print('Get:', get)
main()



