"""My Grade"""
def main():
    """Main function"""
    grade = float(input())
    if grade >= 90:
        print("A")
    if 80 <= grade < 90:
        print("B+")
    if 75 <= grade < 80:
        print("B")
    if 67 <= grade < 75:
        print("C+")
    if 50 <= grade < 67:
        print("C")
    if 40 <= grade < 50:
        print("D+")
    if 30 <= grade < 40:
        print("D")
    if grade < 30:
        print("F")
main()
