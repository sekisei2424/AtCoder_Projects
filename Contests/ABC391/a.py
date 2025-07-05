D = input()

if len(D) == 1:
    if D == "N" or D == "S":
        print("N" if D == "S" else "S")
    else:
        print("E" if D == "W" else "W")
else:
    ans = ""
    if D == "NE":
        print("SW")
    elif D == "NW":
        print("SE")
    elif D == "SE":
        print("NW")
    else:
        print("NE")