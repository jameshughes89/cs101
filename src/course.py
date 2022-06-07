from student import Student


class Course:
    """
    A collection of students enrolled in a course. This class manages the individual Students and provides simple
    enrollment details.
    """

    def __init__(self, course_name: str):
        self.course_name = course_name
        self._students = []

    def size(self) -> int:
        return len(self._students)

    def add(self, student: Student):
        self._students.append(student)

    def find(self, student: Student) -> int:
        """
        Returns the index of the first occurrence of a given Student if it exists. If it does not exist, return a
        sentinel value of -1.

        :param student: The student to search for
        :type student: Student
        :return: Index of the student, or -1 if it is not found
        :rtype: int
        """
        for i, s in enumerate(self._students):
            if s == student:
                return i
        return -1

    def remove(self, student: Student):
        """
        Remove the first occurence of the specified student from the collection. If the student does not exist, raise
        an exception.

        :raise Value error: If the student does not exist within the collection, a ValueError is raised.
        :param student: The student to be removed
        :type student: Student
        """
        index = self.find(student)
        if index == -1:
            raise ValueError("No such student to remove")
        else:
            self._students.pop(index)

    def __repr__(self) -> str:
        s = ""
        for student in self._students:
            s += str(student) + "\n"
        return s
