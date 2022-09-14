vocali = ["a", "e", "i", "o", "u", "xr", "yt"]
def translate_word(text):
    if text[0] in vocali or text[:2] in vocali :
        return text + "ay"
    elif text[0] not in vocali and text[1]=="y":
        return text[1:]+text[0] + "ay"
    elif text[0] not in vocali and  text[1:3]== "qu":
        return text[3:] + text[:3] +"ay"
    elif text[0] not in vocali and text[1] not in vocali and  text[2:3]== "qu": 
        return text[4:] + text[:4] +"ay"
    elif text[:2]== "qu": 
        return text[2:] + text[:2] +"ay"
    elif text[0] not in vocali and  text[1] in vocali:
        return text[1:] + text[0] +"ay"
    elif text[0] not in vocali and text[1] not in vocali and  text[2] in vocali: 
        return text[2:] + text[:2] +"ay"
    elif text[0] not in vocali and  text[1]== "y":
        return text[1:] + text[0] +"ay"
    elif text[0] not in vocali and text[1] not in vocali and  text[2]== "y": 
        return text[2:] + text[:2] +"ay"
    elif text[0] not in vocali and text[1] not in vocali and text[2] not in vocali: 
        return text[3:] + text[:3] +"ay"
def translate(text):
    parole = text.split()
    ret = ""
    for parola in parole:
        ret += translate_word(parola) +" "
    return ret[:-1]