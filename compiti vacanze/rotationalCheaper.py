alfabeto_m = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto_M = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
caratteri = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',', '_', '-', '?', '!', '(', ')', '+', "'", '{', '}', '[', ']', ':']
def rotate(text, key):
    new_text = ""
    for c in text:
        for k in range(len(alfabeto_m)):
            if c == alfabeto_m[k]:
                i = k + key
                if i >25:
                    i = i - 26
                new_text = new_text + alfabeto_m[i]
            elif c == alfabeto_M[k]:
                i = k + key
                if i >25:
                    i = i - 26
                new_text = new_text + alfabeto_M[i]
            elif c == caratteri[k]:
                new_text = new_text + c
    return new_text