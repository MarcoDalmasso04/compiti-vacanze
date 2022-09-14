EXPECTED_BAKE_TIME = 40
def bake_time_remaining(time):
    """Calcola il tempo rimanente di cottura.
   """
    return (40 - time)
def preparation_time_in_minutes(layer):
    """Calcola il tempo di preparazione quando aggiungi un livello.
       2 minuti per livello.
    """
    return (2* layer)
def elapsed_time_in_minutes(layers,t):
    """Calcola il tempo rimanente di cottura aggiungendo il tempo per i ivelli aggiunti.
    """
    return (2* layers + t)
