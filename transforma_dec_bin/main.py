def bin_dec_float(n, l=None):
    if l is None:
        l = list()
    res = int(n) * 2
    l.append((str(res)[0]))
    res = int(res)
    if res >= 1:
        res -= 1
    if res == 0:
        return ''.join(l)
    else:
        res = str(res)
        return bin_dec_float(res, l)


def bin_dec_int(n):
    n = int(n)
    return str(bin(n)[2:])


def bin_dec(n):
    n = str(n)
    comma_pos = n.find('.')
    return bin_dec_int(n[:comma_pos]) + '.' + bin_dec_float(n[comma_pos + 1:])


if __name__ == "__main__":
    print(bin_dec_float(15.25))
