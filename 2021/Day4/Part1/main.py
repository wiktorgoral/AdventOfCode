def win(listt):
    size: int = len(listt)
    flag: bool = True
    # diagonal
    for i in range(size):
        if not listt[i][i]: flag = False
    if flag: return True
    else: flag = True

    for i in range(size):
        if not listt[size - i - 1][size - i - 1]: flag = False
    if flag: return True
    else: flag = False
    # row
    for i in range(size):
        for j in range(size):
            if not listt[i][j]: flag = False
        if flag: return True
        else: flag = True
    # column
    for i in range(size):
        for j in range(size):
            if not listt[j][i]: flag = False
        if flag: return True
        else: flag = True
