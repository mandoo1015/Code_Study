def binary_search(target, data):
    left_index, right_index = 0, len(data) - 1
    while left_index <= right_index:
        mid_idx = (left_index + right_index) // 2
        mid_element = data[mid_idx]
        if target == mid_element:
            return mid_idx
        elif target < mid_element:
            right_index = mid_idx - 1
        elif target > mid_element:
            left_index = mid_idx + 1