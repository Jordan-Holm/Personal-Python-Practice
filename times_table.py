table_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def print_table(list):
    for i in list:
        print(f"{i} multiples", end="\n")
        for j in list:
            print(i * j, end=",")
        print()

print_table(table_nums)