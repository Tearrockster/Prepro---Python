"""The Edge"""
def main():
    """Main function"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = float(input())
    more = max(num1, num2, num3, num4, num5)
    less = min(num1, num2, num3, num4, num5)
    total = num1 + num2 + num3 + num4 + num5
    avr = total / 5
    print("Total: %.2f THB"%total)
    print("Maximum: %.2f THB"%more)
    print("Minimum: %.2f THB"%less)
    print("Average: %.2f THB"%avr)
main()
