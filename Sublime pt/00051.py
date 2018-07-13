""" The Camp EP.2 "Pick Day Pick Me Up!" """
def main():
    """Main function"""
    num1 = int(input())
    if 23 <= num1 <= 25:
        print("Yep! %d UNiTEC@MP3"%num1)
    elif 32 > num1 > 25 or num1 < 23:
        print("Try again!")
    elif num1 > 31:
        print("404 NOT FOUND")
main()
