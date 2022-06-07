class Student:
    """
    Class for storing basic student information. The class serves as a mechanism for storing and returning information
    and checking equality.
    """

    def __init__(self, first_name, last_name, student_number):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number

    def __eq__(self, other) -> bool:
        """
        Two students are considered equal if their student numbers are the same. This assumes student numbers are unique
        among students.

        :param other: A student to compare the self Student to
        :type other: Student
        :return: True if the students have the same student number, false otherwise
        :rtype: boolean
        """
        if isinstance(other, Student):
            return self.student_number == other.student_number
        return False

    def __repr__(self) -> str:
        return f"{self.last_name}, {self.first_name}\t{self.student_number}"
