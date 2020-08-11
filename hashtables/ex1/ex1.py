def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    seen = {}
    for i in range(length):
        seen[weights[i]] = i
    
    for j in range(length):
        curr = weights[j]
        leftover = limit - curr
        if leftover in seen and seen[leftover] != j:
            if seen[leftover] > j:
                return (seen[leftover], j)
            else:
                return (j, seen[leftover])

    return None
