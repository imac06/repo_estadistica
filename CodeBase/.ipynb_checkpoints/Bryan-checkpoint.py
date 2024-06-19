def ordenar_asc(clases):
    
    arr_len = len(clases)

    for i in range(arr_len):
        min_idx = i
        for j in range(i+1, arr_len):
            if clases[j] < clases[min_idx]:
                min_idx = j
        clases[i], clases[min_idx] = clases[min_idx], clases[i]         

    return clases