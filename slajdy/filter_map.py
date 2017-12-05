def is_odd(n):
    return not n % 2

def double(n):
    return n * 2

def triple(n):
    return n * 3

def filter_map(inp, fil, mp):
    result = []
    for i in inp:
        if fil(i):
            i = mp(i)
        result.append(i)
    
    return result;
    
if __name__ == '__main__':
    print(filter_map([3, 4, 8, 11, 13], is_odd, double))
    print(filter_map([3, 4, 8, 11, 13], is_odd, triple))