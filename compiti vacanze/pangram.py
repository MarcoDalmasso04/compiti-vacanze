def is_pangram(sentence):
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in sentence.lower():
            return False
    return True