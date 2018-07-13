"""MRT Blue Line"""

def function():
    """My function"""

    stat = input()
    if "Chatuchak Park" in stat:
        return 21
    if "Phahon Yothin" in stat:
        return 23
    if "Lat Phrao" in stat:
        return 25
    if "Ratchadaphisek" in stat:
        return 28

def function2():
    """My function"""
    station = function()
    typ = input()
    if "Adult" in typ:
        print(station)
    if "Student" in typ:
        print(station - (2 + (1 * station == 28)))
    if "Elder" in typ:
        print(station//2 + (station%2 > 0))

function2()





