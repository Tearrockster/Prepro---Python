"""Match Winner"""
def main():
    """Main function"""
    function(1)
    function(2)
    function(3)
    function(4)
    function(5)
    function(6)

def function(num):
    """My function"""
    nameteam1 = input()
    score1 = int(input())
    nameteam2 = input()
    score2 = int(input())

    if score1 > score2:
        print("Match #%d:"%num, nameteam1)
    elif score2 > score1:
        print("Match #%d:"%num, nameteam2)
    elif score1 == score2:
        print("Match #%d:"%num, "Tie!")
main()

