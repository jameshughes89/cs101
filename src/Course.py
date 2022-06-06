class Course:
    """
    A collection of students enrolled in a course. This class manages the individual Students and provides simple
    enrollment details.
    """

    def __int__(self, course_name):
        self.course_name = course_name
        self._students = []

    