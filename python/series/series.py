def slices(seq, n):

    if n > len(seq) or n == 0:
        raise ValueError
    
    seq = [int(x) for x in list(seq)]
    slice_list = []
    a = 0
    b = n
    while b <= len(seq):
        slice_list.append(seq[a:b])
        a += 1
        b += 1
        
    return slice_list
