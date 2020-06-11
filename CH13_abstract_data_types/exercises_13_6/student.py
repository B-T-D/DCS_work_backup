"""From 13.1.18 originally but doing it here because skipped
and needed for 13.6.12.

Student ADT Attributes:

    <name>| <description>

    name | a string containing the student's name
    exam grades | list
    quiz grades | list
    lab grades | list
    paper grades | list
    
Student ADT Operations:
    <name>| <arguments> | <description>

    create | student's name | create a new Student instance
    add grades | exam quis lab or paper | add a grade to the relevant list
    get name | None | return student's name
    
"""

class Student:

    EXAM_WEIGHT = 0.5
    QUIZ_WEIGHT = 0.1
    LAB_WEIGHT = 0.2
    PAPER_WEIGHT = 0.2

    assert EXAM_WEIGHT + QUIZ_WEIGHT + LAB_WEIGHT + PAPER_WEIGHT == 1,\
    f"Assessment weights must sum to 100%"

    def __init__(self, name):
        """Initialize a Student instance with name and all other instance
        variables as blank lists."""

        self._name = name
        self._exam_grades = []
        self._quiz_grades = []
        self._lab_grades = []
        self._paper_grades = []

    def add_grade(self, grade_type, score):
        """
        Args:
            grade_type (str): whether the grade is exam, quiz, lab, or paper.
            score (int or float): student's grade on the assessment]
        """
        grade_list = self._parse_grade_type(grade_type)
        grade_list.append(score)
        
    def _parse_grade_type(self, grade_type: str):
        """Return the instance variable of self corresponding to that grade type. E.g. if
        grade_type is 'quiz', return the quiz grades list.
        """

        grade_type = grade_type.lower()
        if grade_type == 'exam':
            collection = self._exam_grades
        elif grade_type == 'quiz':
            collection = self._quiz_grades
        elif grade_type == 'lab':
            collection = self._lab_grades
        elif grade_type == 'paper':
            collection = self._paper_grades
        else:
            raise ValueError("grade_type must be one of exam, quiz, lab, or paper")
        return collection

    def avg_grade(self, grade_type: str):
        """Return the average score on assessments of grade_type.

        Treat blank components as a score of zero.
        """
        grade_list = self._parse_grade_type(grade_type)
        if len(grade_list) == 0:
            return 0
        else:
            sum = 0
            for grade in grade_list:
                sum += grade
            return sum / len(grade_list)

    def final_grade(self):
        """Return the student's final grade in the course."""
        exam_avg = self.avg_grade('exam')
        quiz_avg = self.avg_grade('quiz')
        lab_avg = self.avg_grade('lab')
        paper_avg = self.avg_grade('paper')
        return exam_avg * self.EXAM_WEIGHT +\
               quiz_avg * self.QUIZ_WEIGHT +\
               lab_avg * self.LAB_WEIGHT +\
               paper_avg * self.PAPER_WEIGHT
        
    def get_name(self):
        return self._name

    def all_grades(self):
        """Return all of the student's grades on all assessments.

        Returns:
            (dict): assessment_type: [list of grades]"""
        grades = {}
        grades['exam'] = self._exam_grades
        grades['quiz'] = self._quiz_grades
        grades['lab'] = self._lab_grades
        grades['paper'] = self._paper_grades
        return grades

def main():
    bill = Student('Bill')
    print(bill._exam_grades)
    bill.add_grade('exam', 17)
    print(bill._exam_grades)
    bill.add_grade('exam', 100)
    print(bill.avg_grade('exam'))

    # Student who got 100% on everything, then 0 on quizzes, should get a
    #   90 final grade in the course.
    alice = Student('Alice')
    for i in range(3):
        alice.add_grade('exam', 100)
        alice.add_grade('lab', 100)
        alice.add_grade('paper', 100)
    for i in range(500): # Quizzes are only 10% of the grade no matter how many quizzes there are
        alice.add_grade('quiz', 0)
    expected = 90
    actual = alice.final_grade()
    assert actual == expected, f"actual {actual}, expected {expected}"

    # Student who got 0 on the exam and 100 on everything else should get
    #   50 final grade.
    failson = Student('Failson')
    for i in range(10):
        failson.add_grade('lab', 100)
        failson.add_grade('paper', 100)
        failson.add_grade('quiz', 100)
    failson.add_grade('exam', 0)
    expected = 50
    actual = failson.final_grade()
    assert actual == expected, f"actual {actual}, expected {expected}"

if __name__ == '__main__':
    main()
    
