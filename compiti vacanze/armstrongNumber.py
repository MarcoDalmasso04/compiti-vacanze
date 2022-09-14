def is_armstrong_number(number):
    num = str(number)
    sum = 0
    for cifra in num:
        sum += int(cifra) ** len(num)
    return sum == number