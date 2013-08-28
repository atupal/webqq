
def hexchar2bin(str):
    ret = ''
    arr = []
    i = 0
    while i < len(str):
        arr.append("\\x" + str[i:i+2])
        i += 2

    arr = "".join(arr)


    return ret


def encryp_1(pwd):
    ret = ''
    return ret


