
def show_numbers(limit):
    limit = int(input('enter a number: '))
    for i in range(0, limit+1):
        if i % 2 == 0:
            print(i, " EVEN")
        else:
            print(i, " ODD")

show_numbers(0)