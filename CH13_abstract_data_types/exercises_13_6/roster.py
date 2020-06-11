"""Exercise 13.6.12"""

import student as s

class Roster:
    """Stores information about all students in a course. Students are
    represented as Student objects using class from 13.1 exercise."""

    _SID = 0 # the SID number will always be element [0] in the tuple
    _STUDENT = 1 # Student obj will always be element [1]
    
    def __init__(self):

        self._length = 0 # number of Student-id pairs
        self._size = 383 # a large-ish prime number for hashing
        self._students = [None] * self._size # list of the Student objects.
        # ^ each element will be a tuple (id, Student object)
        self._length = 0

        # ^^ Book implements it as simply two lists. One list of students,
        #   one list of ids. They're only ever linked by a common index
        #   value when something is referencing them. 

    def _hash(self, sid):
        """Hash the given sid number."""
        # using the builtin python hash(x) for now
        return hash(sid) # will fail if sid were a mutable type but ints are immutable

    def __setitem__(self, sid, student):
        """
        Called with e.g. roster[101] = alice where alice is a Student object.
        Args:
            sid (int): student ID number
            student (Student): a student object.
        """
        index = self._hash(sid)
        self._students[index] = (sid, student)
        self._length += 1

    def __getitem__(self, sid):
        """Return the Student object associated with the given sid number."""

        index = self._hash(sid)
        if self._students[index] != None \
           and self._students[index][self._SID] == sid:
            return self._students[index][self._STUDENT]
        else:
            raise KeyError("SID was not found.")

    def __len__(self):
        return self._length

    def avg_exam(self):
        """Returns the average of all the exam grades for all of the
        students."""
        sum = 0
        for index in range(self._size):
            if self._students[index] != None:
                student = self._students[index][self._STUDENT]
                print(f"student is {student}")
                sum += student.avg_grade('exam')
                print(f"sum is now {sum}")
        return sum / len(self)

    def avg_grade(self):
        """Returns the average overall grade for all the students."""
        sum = 0
        for index in range(self._size):
            if self._students[index] != None:
                sum += self._students[index][self._STUDENT].final_grade()
        return sum / len(self)
                

    def __str__(self):
        """Return a string represnting the complete roster with current
        grades."""
        string = ''
        for i in range(self._size):
            if self._students[i] != None:
                string += str(self._students[i][self._SID]) + '\t' + \
                           self._students[i][self._STUDENT].get_name() + '\t' + \
                           str(self._students[i][self._STUDENT].all_grades())
                string += '\n' # new line for each student
        return string
                           
def main():
    roster = Roster()
    alice = s.Student('Alice Miller')
    bob = s.Student('Bob Smith')
    charles = s.Student('Charles Charleston')
    roster[101] = alice
    roster[101].add_grade('exam', 85)
    roster[102] = bob
    roster[102].add_grade('exam', 100)
    print(roster.avg_exam())
    print(roster.avg_grade())
    roster[103] = charles
    roster[103].add_grade('exam', 76)
    print(roster[101])
    print(roster.avg_exam())
    print(roster.avg_grade())
    print(roster)

if __name__ == '__main__':
    main()
        
        
