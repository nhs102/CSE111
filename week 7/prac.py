import random

def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)

    quantity = 1
    append_random_numbers(randnums, quantity)
    print(randnums)
    
    quantity = 3
    append_random_numbers(randnums,quantity)
    print(randnums)


def append_random_numbers(numbers_list, quantity):
    for _ in range(quantity):
        random_num = random.uniform(0, 100)
        rounded = round(random_num, 1)
        numbers_list.append(rounded)

if __name__ == "__main__":
    main()