def number_length(num):
    counter = 0
    if num == 0:
        return 1
    while num != 0:
        counter += 1
        num //= 10
    return counter


print(number_length(10))
