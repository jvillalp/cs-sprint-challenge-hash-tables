def intersection(arrays):
    """
    YOUR CODE HERE
    """
    num_lists = len(arrays)
    seen = {}
    result = []
    for i in range(num_lists):
        for j in range(len(arrays[i])):
            if arrays[i][j] in seen:
                seen[arrays[i][j]].append(i)
            else:
                seen[arrays[i][j]] = [i]
    
    for key in seen:
        if len(seen[key]) == num_lists:
            result.append(key)
    #return list of all integers in lists that are the same
    return result




if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
