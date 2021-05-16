def quick_sort(array, start_idx, end_idx):
    pivot = start_idx
    pointer = end_idx

    while pivot != pointer:
        if array[pointer] < array[pivot] and pointer > pivot:
            array[pointer], array[pivot] = array[pivot], array[pointer]
            pointer, pivot = pivot, pointer

        elif array[pointer] > array[pivot] and pointer < pivot:
            array[pointer], array[pivot] = array[pivot], array[pointer]
            pointer, pivot = pivot, pointer

        if pointer > pivot:
            pointer -= 1
        else:
            pointer += 1

    if start_idx < pivot:
        quick_sort(array, start_idx, pivot - 1)

    if end_idx > pivot:
        quick_sort(array, pivot + 1, end_idx)


def binary_search(array, start, end, value):
    middle = (start + end) // 2

    if value == array[middle]:
        return middle

    if start == end or middle == -1:
        return -1

    if value < array[middle]:
        return binary_search(array, start, middle - 1, value)
    else:
        return binary_search(array, middle + 1, end, value)


medicinas_length, peticiones = input().split()
medicinas = input().split()

# Ordenando las medicinas
quick_sort(medicinas, 0, len(medicinas) - 1)
indices = []

for _ in range(0, int(peticiones)):
    medicina = input()
    # Busqueda de medicinas
    value = binary_search(medicinas, 0, int(medicinas_length) - 1, medicina)
    indices.append(value)

for indice in indices:
    print(indice)
