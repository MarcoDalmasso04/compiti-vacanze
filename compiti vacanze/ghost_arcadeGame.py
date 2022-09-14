def eat_ghost(power_pellet_active, touching_ghost):
    """Verifica che Pac-Man possa mangiare un fantasma se è potenziato da un power 
       pellet.
    """

    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Verifica che Pac-Man abbia segnato quando attiva un power pellet o un punto è stato 
       mangiato
    """

    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Quando pac-man tocca un fantasma senza il power pellet, la partita finisce.
    """

    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Quando pac-man mangia tutti i punti, la partita finisce con una vittoria
    """

    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)