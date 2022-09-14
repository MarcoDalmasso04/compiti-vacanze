def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    
    prefisso = vocab_words[0]
    n = len(vocab_words)
    parola = ""
    parola += prefisso
    for k in range(1, n):
        parola += " " + "::" + " " + prefisso + vocab_words[k]
    return parola

def remove_suffix_ness(word):
    
    return word[:-4] if word[-5] != 'i' else word[:-5]+'y' 