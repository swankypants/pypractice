def prime_number(limit):
    for prime in range(2, limit + 1):
        for num in range(2, prime):
            if prime % num == 0:
                break
        else:
            print(prime)

prime_number(15)
