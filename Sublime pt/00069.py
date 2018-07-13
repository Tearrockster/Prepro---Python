"""Skipping"""
def main():
    """Main function"""
    room = int(input())
    student = int(input())

    for i in range(1, room + 1, student):
        print(i)
main()

