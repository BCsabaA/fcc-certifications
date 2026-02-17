def selection_sort(array: list) -> list:
    if len(array) in (0, 1):
        return array

    def minimum(l: list):
        l_min = l[0]
        index = 0
        for i, element in enumerate(l):
            if element < l_min:
                l_min = element
                index = i
        return l_min, index
                
    for i in range(len(array)-1):
        rest_min, rest_min_index = minimum(array[i+1:])
        if array[i] > rest_min:
            t = array[i]
            array[i] = array[rest_min_index + i + 1]
            array[rest_min_index + i + 1] = t
    return array


# numbers = [3, 2, 1]
# print(selection_sort(numbers))
# print(numbers)
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))
# print(selection_sort([1, 4, 2, 1]))
