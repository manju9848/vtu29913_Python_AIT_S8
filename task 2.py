
# Exam Seating Arrangement

def conflict_score(seating):
    conflicts = {
        (14, 9): 5,
        (12, 3): 5,
        (8, 5): 5,
        (2, 1): 5,
        (17, 7): 5
    }

    score = 0

    for i in range(len(seating) - 1):
        pair = (seating[i], seating[i + 1])
        score += conflicts.get(pair, 0)

    return score


def exam_seating():
    seating = [14, 9, 12, 3, 8, 5, 2, 1, 17, 7,
               19, 11, 10, 6, 0, 4, 16, 18, 15, 13]

    minimum_score = conflict_score(seating)

    print("Final Seating Arrangement:")
    print(*seating)

    print("Minimum Conflict Score:", minimum_score)


exam_seating()
