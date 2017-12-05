def primes(n):
    result = []
    i = 2
    while len(result)<n:
        is_prime = True
        for prime in result:
            if not i % prime:
                is_prime = False
                break
        if is_prime:
            result.append(i)
        i += 1
    return result

print(primes(10))