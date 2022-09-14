def is_valid(isbn):
    sum = 0
    n = 10
    isbn = isbn.replace('-','')
    if isbn == '' or len(isbn) != 10:
        return False
    for num in isbn:
        if num.isalpha():
            if num == 'X':
                sum += 10
            else:
                return False
        else:
            sum += int(num) * n
            n -= 1
    return sum % 11 == 0