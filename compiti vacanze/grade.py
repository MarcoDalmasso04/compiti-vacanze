def round_scores(student_scores):
    rdd_scores = []
    for score in student_scores:
        rdd_scores.append(round(score))
    return rdd_scores
    
def count_failed_students(student_scores):
    cont = 0
    for score in student_scores:
        if score <= 40:
            cont += 1
    return cont
    
def above_threshold(student_scores, threshold):
    maggiori = []
    for score in student_scores:
        if score >= threshold:
            maggiori.append(score)
    if maggiori != []:
        return maggiori
    return []
    
def letter_grades(highest):
    limits = []
    increment = int((highest -40)/4)
    for i in range(4):
        limit = 41 + i * increment
        limits.append(limit)
    return limits
    
def student_ranking(student_scores, student_names):
    '1. Joci: 100', '2. Sara: 99', 
    ranking_list = []

    for k in range(0, len(student_scores)):
        ranking_list.append(f"{k + 1}. {student_names[k]}: {student_scores[k]}")
    
    return ranking_list
    
def perfect_score(student_info):
    for perfect in student_info:
        if perfect[1] == 100:
            return perfect
    return []