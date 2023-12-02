def area(side01, side02) :
    area = side01 * side02
    print(f"The area of the rectangle is {area}m²")

weight = float(input("What's the weight of the rectangle?\n").strip())
height = float(input("What's the height of the rectangle?\n").strip())

area(weight, height)
