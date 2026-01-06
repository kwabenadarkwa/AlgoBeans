def find_smallest(arr: list) -> int:
    return arr.index(min(arr))


def selection_sort(arr: list) -> list:
    return_arr = []
    initial_array_len = len(arr)
    for _ in range(initial_array_len):
        smallest_index = find_smallest(arr)
        return_arr.append(arr.pop(smallest_index))
        
    return return_arr

if __name__ == "__main__":
    print(selection_sort([220,54,10,10,29,114]))
