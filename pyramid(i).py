def print_star_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()


num_rows = 5

print_star_triangle(num_rows)
