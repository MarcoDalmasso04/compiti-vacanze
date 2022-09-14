def convert(number):
    risposta = ""
    if number % 3 == 0:
        risposta += "Pling"
    if number % 5 == 0:
        risposta += "Plang"
    if number % 7 == 0:
        risposta += "Plong"
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        risposta = str(number)
    
    return risposta