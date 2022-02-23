
def multiple_sum(limit):
    num_range = 0
    for i in range(limit + 1):
        if i % 3 == 0 or i % 5 == 0:
            print(i)
    return num_range


multiple_sum(20)

