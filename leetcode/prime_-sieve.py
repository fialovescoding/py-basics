
def seive_of_erathosthenes(max: int):
    # We create a dictionary, and set key=1, value=False, which means 1 is not prime
    primes = {1: False}
    # For all other numbers from 2 to max, set value to None
    for i in range(2, max + 1):
        primes[i] = None

    # Now check every number from 2 to max
    p = 2
    while p < max + 1:
        # If we've not yet set primes[p] to True or False
        if primes[p] is None:
            # Set true
            primes[p] = True
            # k is a multiplier, starting with 2, so all multiples of p are composite
            k = 2
            while (p * k) < max:
                m = p * k
                primes[m] = False
                k = k + 1
        p = p + 1

    return [p for p in primes.keys() if primes[p]]

max = 73
print(seive_of_erathosthenes(max)) 