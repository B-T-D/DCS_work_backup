"""
Ex 3.5.12
2020-03-28 21:17
"""

def grade_point(score):
    
    if score >= 90:
        gp = 4
    elif score >= 80:
        gp = 3
    elif score >= 70:
        gp = 2
    elif score >= 60:
        gp = 1
    else:
        gp = 0
    return int(gp)

def grade_point(score):
    cutoffs = {90: 4, 80: 3, 70: 2, 60: 1, 0: 0}
    for key, value in cutoffs.items():
        if score >= key:
            return value
# AK's:
def grade_point(score):
    return max(score // 10 - 5, 0)

for i in (94, 87, 70, 69, 12):
    print(f"Score of {i} is grade point of {grade_point(i)}")
