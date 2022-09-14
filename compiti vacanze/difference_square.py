def square_of_sum(number):
    s = 0
    for n in range(0, number + 1):
        s = s + n
    return s ** 2

def sum_of_squares(number):
    s = 0
    for n in range(0, number + 1):
        s = s + n ** 2
    return s

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
