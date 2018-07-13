"""Past Tense"""
def main():
    """Main function"""
    sentence = input().lower()
    change1 = sentence.replace('is', 'was')
    change2 = sentence.replace('are', 'were')


    if "is" in sentence and sentence.find('is'):
        print(change1)
    if "are" in sentence:
        print(change2)

main()

