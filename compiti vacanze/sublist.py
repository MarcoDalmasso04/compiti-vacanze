
SUBLIST = 'sublist'
SUPERLIST = 'superlist'
EQUAL = 'equal'
UNEQUAL = 'unequal'
def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif len(list_one) > len(list_two):
        maggiore = list_one
        minore = list_two
    else:
        maggiore = list_two
        minore = list_one
    for i in range(0, len(maggiore)):
        if maggiore[i:i + len(minore)] == minore and maggiore == list_one:
            return SUPERLIST
        elif maggiore[i:i + len(minore)] == minore and maggiore == list_two:
            return SUBLIST
    return UNEQUAL