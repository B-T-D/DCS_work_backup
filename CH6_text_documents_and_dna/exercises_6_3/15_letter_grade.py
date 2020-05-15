def letter_grade(grade):
    if grade >= 100:
        return 'A'
    if grade > 59:
        return chr(grade - (grade - ord('A')))
    return 'F'

def sol_man(grade):
    if (grade < 0) or (grade > 100):
        return None
    if grade == 100:
        return 'A'
    if grade < 60:
        return 'F'
    return chr(9 - int(grade / 10) + ord('A'))

for i in range(100, 0, -3):
    print(f"{i} | {sol_man(i)}")
