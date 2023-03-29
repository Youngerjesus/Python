out_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def split_n_list(split_list_size=3):
    split_list = list()

    for i in range(0, len(out_list), split_list_size):
        split_list.append(out_list[i:i+split_list_size])

    return split_list

print(split_n_list())

print([out_list[i:i+3] for i in range(0, len(out_list), 3)])