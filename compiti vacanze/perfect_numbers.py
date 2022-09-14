def classify(number):
    somma = 0
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    for n in range(1, number):
        if number % n == 0:
            somma += n
    if somma == number:
        return "perfect"
    elif somma > number:
        return "abundant"
    else:
        return "deficient"