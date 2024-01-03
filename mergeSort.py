def merge_sort(unsorted_array):
    if len(unsorted_array) > 1:
        mid = len(unsorted_array) // 2
        left = unsorted_array[:mid]
        right = unsorted_array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_array[k] = left[i]
                i += 1
            else:
                unsorted_array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_array[k] = right[j]
            j += 1
            k += 1

def print_list(array1):
    for i in range(len(array1)):
        print(array1[i], end=" ")
    print()

if __name__ == '__main__':
    array = [23, 22, 24, 29, 76, 97]
    print("Matricea dată este:", end="\n")
    print_list(array)
    merge_sort(array)
    print("Matricea sortată este: ", end="\n")
    print_list(array)