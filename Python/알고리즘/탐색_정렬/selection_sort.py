def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]: 
                min_idx = j
        if min_idx != i:
            data[min_idx], data[i] = data[i], data[min_idx]