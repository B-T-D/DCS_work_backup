import random

def compute_grades(scores):

    grades = []

    for score in scores:
        if score >= 90:
            grades.append('A')
        elif score >= 80:
            grades.append('B')
        elif score >= 70:
            grades.append('C')
        elif score >= 60:
            grades.append('D')
        elif score < 60:
            grades.append('F')

    return grades

def random_scores(n):
    scores = []
    for count in range(n):
        scores.append(random.gauss(80, 10))
    return scores

for i in range(6):
    n = 10 ** i
    scores = random_scores(n)
    print(f"at n of {n}, lowest score was {min(scores)}")
    
n = 100
scores = random_scores(n)
grades = compute_grades(scores)
print(grades)


