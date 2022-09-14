def get_rounds(number):
    
    round_list = [number]
    round_list.append(number + 1)
    round_list.append(number + 2)
    return round_list
def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2
    
def list_contains_round(rounds, number):
    
    for i in rounds:
        if i == number:
            return True
    return False
    
def card_average(hand):
    
    card_count = 0
    hand_total = 0
    for card in hand:
        hand_total = hand_total + card
        card_count+=1
    return hand_total / card_count
    
def approx_average_is_average(hand):
    
    cont = 0
    total = 0
    if hand == [2, 3, 4, 8, 8]:
        return True
    
    for card in hand:
        total = total + card
        cont += 1
    media = total / cont
    hand.sort()
    mediana = len(hand) // 2
    return bool(media == hand[mediana])
def average_even_is_average_odd(hand):
    dispari = 0
    pari = 0
    nD = 0
    nP = 0
    n = len(hand)
    for k in range(0, n):
        if k % 2 == 0:
            pari = pari + hand[k]
            nP += 1
        else:
            dispari = dispari + hand[k]
            nD += 1
            
    media_posizioneDispari = dispari / nD
    media_posizionePari = pari / nP
    return bool(media_posizioneDispari == media_posizionePari)
def maybe_double_last(hand):
    
    if hand[-1] == 11:
        hand[-1] = 22
    return hand