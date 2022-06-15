from src.student import Student


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

    def _find(self, student: Student) -> int:
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

    def contains(self, student: Student) -> bool:
        """
        Checks if a given student exists within the Course.

        :param student: The Student object to be checked if it exists within the Course
        :type student: Student
        :return: True if the Student exists, False otherwise
        :rtype: bool
        """
        return -1 != self._find(student)

    def remove(self, student: Student):
        """
        Remove the first occurence of the specified student from the collection. If the student does not exist, raise
        an exception.

        :raise Value error: If the student does not exist within the collection, a ValueError is raised.
        :param student: The student to be removed
        :type student: Student
        """

        if not self.contains(student):
            raise ValueError("No such student to remove")
        else:
            self._students.pop(self._find(student))

    def __repr__(self) -> str:
        s = ""
        for student in self._students:
            s += str(student) + "\n"
        return s
