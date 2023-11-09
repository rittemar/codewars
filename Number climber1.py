def climb(n):
    #For every positive integer N, there exists a unique sequence starting with 1 and ending
    # with N and such that every number in the sequence is either the double of the preceeding
    # number or the double plus 1. Function climbs to N, starting at 1.
    if n == 1:
        return [1]
    start_num = 1
    counter = 1
    final_lst = [1]
    while start_num < n:
        if counter == 1 or counter % 2 != 0:
            temp1 = start_num * 2 + 1
            start_num = temp1
            final_lst.append(start_num)
            counter += 1
        elif counter % 2 == 0:
            temp2 = start_num * 2
            start_num = temp2
            final_lst.append(start_num)
            counter += 1
    return final_lst



climb(13)