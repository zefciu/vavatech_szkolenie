def skip(inp, interval=2):
    result = []
    idx = 0    
    for i, element in enumerate(inp):
        if i % interval == 0:
            result.append(element)
                
        idx += 1
    
    return result;


if __name__ == '__main__':
    print(skip(range(20)))
    print(skip(range(20), 3))
    print(skip([3,6,5,2,3,6,8,9], 3))