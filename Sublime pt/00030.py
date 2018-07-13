"""
Dog Lovers
"""
def main():
    """Mainfunction"""
    total = 0
    food1, food2 = int(input()), int(input())
    total += discount(food1, food2)
    food1, food2 = int(input()), int(input())
    total += discount(food1, food2)
    food1, food2 = int(input()), int(input())
    total += discount(food1, food2)
    food1, food2 = int(input()), int(input())
    total += discount(food1, food2)

def discount(dogfood1, dogfood2):
    """This Function to discount price"""
    price_bf = dogfood1 + dogfood2
    disc = price_bf * (15/100)


main()