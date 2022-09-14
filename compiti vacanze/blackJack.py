def value_of_card(card):
    if card == 'A':
        card = 1;
    return 10 if card in ('J','Q','K') else int(card)
    
def higher_card(card_one, card_two):
    
    if value_of_card(card_one) > value_of_card(card_two):
        valore = card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        valore = card_two
    else: 
        return card_one, card_two
    return valore 
def value_of_ace(card_one, card_two):
    
    valore_card_one = 11 if card_one == ('A') else value_of_card(card_one)
    valore_card_two = 11 if card_two == ('A') else value_of_card(card_two)   
    punteggio = valore_card_one + valore_card_two + 11
    return 1 if punteggio > 21 else 11
def is_blackjack(card_one, card_two):
    
    value_card_one = 11 if card_one == ('A') else value_of_card(card_one)
    value_card_two = 11 if card_two == ('A') else value_of_card(card_two)   
    punteggio = value_card_one + value_card_two
    return punteggio == 21 
def can_split_pairs(card_one, card_two):
    
    return value_of_card(card_one) == value_of_card(card_two)
def can_double_down(card_one, card_two):
    
    punteggio = value_of_card(card_one) + value_of_card(card_two)
    return punteggio in (9,10,11)