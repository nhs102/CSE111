def main():
    amount_rect = int(input("How many rectangles would you like to make?: "))
    total = 0
    for i in range(1, amount_rect+1):
        side_1 = int(input("what is the length of side 1?: "))
        side_2 = int(input("what is the length of side 2?: "))
        total += area_rectangle (side_1, side_2)
    print(f"your total area is {total}")


def area_rectangle(length,width):
    area = length * width
    print(f"the area is {area}")
    return area

main()