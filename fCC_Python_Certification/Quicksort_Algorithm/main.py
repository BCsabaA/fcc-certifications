def quick_sort(unsorted: list):
    if unsorted == []:
        return []
    if len(unsorted) == 1:
        return unsorted
    pivot = unsorted[0]
    lower_part = [element for element in unsorted if element < pivot]
    equal_part = [element for element in unsorted if element == pivot]
    greater_part = [element for element in unsorted if element > pivot]
    print(f'{lower_part=}\n{equal_part=}\n{greater_part=}')

    sorted_list = []
    sorted_list.extend(quick_sort(lower_part))
    sorted_list.extend(equal_part)
    sorted_list.extend(quick_sort(greater_part))
    return sorted_list


print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))
