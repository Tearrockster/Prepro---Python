"""Dorm EP.2 Latency"""
def main():
    """Main function"""
    lat1 = int(input())
    lat2 = int(input())
    lat3 = int(input())
    lat4 = int(input())
    lat5 = int(input())
    lat6 = int(input())
    latalt = min(lat1, lat2, lat3, lat4, lat5, lat6)
    print("%d ms"%latalt)
main()


