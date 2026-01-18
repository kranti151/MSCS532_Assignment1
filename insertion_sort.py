#Name : Komalben Suthar

def insertion_sort_decreasing(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements that are smaller than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("Original array:", data)
    sorted_data = insertion_sort_decreasing(data)
    print("Sorted array (decreasing):", sorted_data)


