"""The Camp EP.4"""
def main():
    """Main function"""
    namesur = input()
    space = namesur.find(" ")#find spacebar
    amount = len(namesur)#amount of chr namesur
    name = namesur[0:space]#recieve name only 
    wordinfront = namesur[space + 1]#need alphabet first of surname

    print("%s.%s"%(wordinfront, name))

main()
