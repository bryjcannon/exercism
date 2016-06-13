def sum_of_multiples(n, multiples):

    final_list = [0]
    for i in multiples:
        if i == 0:
            continue
        total = i
        count = 1
        while total < n:
            final_list.append(i*count)
            count += 1
            total = i*count
    return sum(set(final_list))
