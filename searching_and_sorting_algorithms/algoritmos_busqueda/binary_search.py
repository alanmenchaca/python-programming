class BinarySearch:

    @staticmethod
    def binary_search(array, start, end, value):
        middle = (start + end) // 2

        if value == array[middle]:
            return array[middle]

        if start == end:
            return -1

        if value < array[middle]:
            return BinarySearch.binary_search(array, start, middle - 1, value)
        else:
            return BinarySearch.binary_search(array, middle + 1, end, value)
