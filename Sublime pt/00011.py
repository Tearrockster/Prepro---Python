"""Dorm EP.3-Average"""
def main():
    """Main function"""
    spt1 = float(input())
    spt2 = float(input())
    spt3 = float(input())
    spt4 = float(input())
    spt5 = float(input())
    spt6 = float(input())
    allspt = spt1 + spt2 + spt3 + spt4 + spt5 + spt6
    alt = allspt / 6
    print("%.2f Mbps" %alt)
main()
