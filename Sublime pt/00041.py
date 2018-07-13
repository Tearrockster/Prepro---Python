"""Did someone say something?"""
def main():
    """Main function"""
    sentence = input()
    joey_topic = input()
    if joey_topic in sentence:
        print("Did someone say %s?"%joey_topic)
    else:
        print("That didn't work.")
main()
