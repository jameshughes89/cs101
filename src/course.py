class Course:
    """
    A collection of students enrolled in a course. This class manages the individual Students and provides simple
    enrollment details.
    """

    def __int__(self, course_name):
        self.course_name = course_name
        self._students = []

    def size(self):
        return len(self._students)

    def add(self, student):
        self._students.append(student)

    def find(self, student):
        for i, s in enumerate(self._students):
            if s == student:
                return i
        return -1

    def remove(self, student):
        index = self.find(student)
        if index == -1:
            raise ValueError("No such student to remove")
        else:
            self._students.pop(index)

    def __repr__(self):
        s = ""
        for student in self._students:
            s += str(student)
        return s
