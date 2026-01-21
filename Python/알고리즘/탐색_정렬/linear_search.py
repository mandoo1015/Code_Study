def linear_search(target, data):
    for idx in range(len(data)):
        if target == data[idx]:
            return idx