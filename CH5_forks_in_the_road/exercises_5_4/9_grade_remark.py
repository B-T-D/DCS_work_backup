def grade_remark():

    grade = float(input('Enter the grade: '))
    remark = 'Trollish'

    if grade >= 80:
        remark = 'Acceptable'
    if grade >= 90:
        remark = 'Exceeds expectations'
    if grade >= 96:
        remark = 'Outstanding'

    return remark

##for i in [70, 79, 90, 91, 81, 85, 96, 97]:
##    print(f"{i} | {grade_remark(i)}")

print(grade_remark())
