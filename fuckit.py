num = 15
width = len(str(num))      # 2 for 15, 3 for 100, etc.

for i in range(num):
    j = 0
    num_list = []

    while j <= i:
        num_list.append(f"{j+1:>{width}}")   # Right-align each number
        j += 1

    no_of_spaces = num - len(num_list)

    while no_of_spaces != 0:
        num_list.append(" " * width)         # Blank space of same width
        no_of_spaces -= 1

    final_list = " ".join(num_list + num_list[::-1])

    print(final_list)