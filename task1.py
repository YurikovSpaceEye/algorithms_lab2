def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    iterations = 0
    while low <= high:

        iterations += 1

        mid = (high + low) // 2

        # Если x больше, игнорируй левую часть
        if arr[mid] < x:
            low = mid + 1

        # Если x меньше, игнорируй правую часть
        elif arr[mid] > x:
            high = mid - 1

        # x означает что индекс x является mid
        else:
            return mid, iterations

    # Если тут, то элемент не находится в массиве.
    return -1, iterations

def verbose_check(arr, x):
    (result_index, iterations) = binary_search(arr, x)

    if result_index == -1:
        print(f"Элемент не находится в массиве. Затрачено {iterations} итераций")
    else:
        print(f"Элемент находится в массиве под индексом {result_index}. Затрачено операций {iterations}")

arr = [i for i in range(10000)]
x = 4189

verbose_check(arr, x)