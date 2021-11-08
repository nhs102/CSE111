import math

num_items = int(input("Enter the number of items: "))
num_items_box = int(input("Enter the number of items per box: "))

num_box = math.ceil(num_items / num_items_box)

print(f"For {num_items:.0f}, packing {num_items_box:.0f} items in each box, you will need {num_box:.0f} boxes.")