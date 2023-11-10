def climb(n):
    #For every positive integer N, there exists a unique sequence starting with 1 and ending
    # with N and such that every number in the sequence is either the double of the preceeding
    # number or the double plus 1. Function climbs to N, starting at 1.
    if n == 1:
        return [1]
    start_num = n
    final_number = n
    final_lst = []
    while start_num > 1:
        if start_num % 2 != 0:
            temp1 = (start_num - 1) / 2
            start_num = int(temp1)
            final_lst.append(start_num)
        if start_num % 2 == 0:
            temp1 = start_num / 2
            start_num = int(temp1)
            final_lst.append(start_num)
    final_lst.reverse()
    final_lst.append(final_number)
    return final_lst

climb(100)