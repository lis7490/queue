from random import randint
import timeit

# Сортировка слиянием
def MergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        MergeSort(left_half)
        MergeSort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len (right_half):
            if left_half[i] < right_half [j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Сортировка пузырьком
def bubble(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr
    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
    if not swapped:
        return arr

    return bubble(arr, n - 1)



ten = []
for i in range(10):
    arr = ten
    ten.append(randint(0, 100))

hundred = []
for i in range(100):
    arr = hundred
    hundred.append(randint(0, 1000))

thousand = []
for i in range(100):
    arr = thousand
    thousand.append(randint(0, 10000))


def Msearch():
    arr =  ten             # сюда подставляем все списки
    MergeSort(arr)

def Bsearch():
    arr =  ten             # сюда подставляем все списки
    bubble(arr)



print(f"Время сортировки слиянием: {timeit.timeit(stmt = "Msearch()", globals=globals(), number = 1000)} сек.")
print(f"Время сортировки пузырьком: {timeit.timeit(stmt = "Bsearch()", globals=globals(), number = 1000)} сек.")


# Тысяча:
# Время сортировки слиянием: 0.06978800000069896 сек.
# Время сортировки пузырьком: 0.0026287000000593252 сек.

# Сто:
# Время сортировки слиянием: 0.07156289999693399 сек.
# Время сортировки пузырьком: 0.002932600000349339 сек.

# Десять:
# Время сортировки слиянием: 0.0046791999993729405 сек.
# Время сортировки пузырьком: 0.0004216999950585887 сек.
