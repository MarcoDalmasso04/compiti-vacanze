def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    errors = 0
    for k in range(0, len(strand_a)):
        if strand_a[k] != strand_b[k]:
            errors += 1
    return errors