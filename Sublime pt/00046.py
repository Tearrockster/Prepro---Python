"""BTS Skytrain EP.3"""
def main():
    """Main function"""
    time = int(input())
    retime = time + 10
    if  retime > 60:
        print("Late!")
    if retime <= 60:
        print("On Time")
main()



