def FFF(n):
    """Faster method of finding factors of a number n"""
    if n == 1:
        return [1]
        
    m = n
    k = 2
    factors = {m}
    while k < m:
        print(f'Check if {k} is a factor of {m}')
        if m % k == 0:
            factors.add(k)
            # Call myself with m = n / k
            m = int(m / k)
            other_f = FFF(m)
            factors = factors.union(other_f)
        
        k = k + 1

    factors.add(1)
    return factors

print(FFF(6034))