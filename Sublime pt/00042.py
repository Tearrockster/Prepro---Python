"""Empty Fridge"""
def main():
    """Main function"""
    cola = int(input())
    tea = int(input())
    orange = int(input())
    straw = int(input())
    milk = int(input())
    print("-Shopping List-")
    if 12 - cola != 0:#have difference
        num = 12 - cola
        print("Cola x%d"%num)
    if 16 - tea != 0:
        num1 = 16 - tea
        print("Tea x%d"%num1)
    if 20 - orange != 0:
        num2 = 20 - orange
        print("Orange Juice x%d"%num2)
    if 24 - straw != 0:
        num3 = 24 - straw
        print("Strawberry Juice x%d"%num3)
    if 32 - milk != 0:
        num4 = 32 - milk
        print("Milk x%d"%num4)

main()

