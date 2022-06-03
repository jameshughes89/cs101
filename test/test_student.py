import unittest

from src.student import Student


class TestStudent(unittest.TestCase):
    def test_equals_on_students_with_same_student_number_returns_true(self):
        student_a = Student("a", "student", 123456789)
        student_b = Student("b", "student", 123456789)
        self.assertTrue(student_a == student_b)

    def test_equals_on_students_with_different_student_numbers_returns_false(self):
        student_a = Student("a", "name", 123456789)
        student_b = Student("a", "name", 987654321)
        self.assertFalse(student_a == student_b)

    def test_equals_on_student_and_string_returns_false(self):
        self.assertFalse("Smith, Bob\t123456789" == Student("Bob", "Smith", 123456789))

    def test_repr_arbitrary_student_returns_correct_string(self):
        student = Student("Bob", "Smith", 123456789)
        self.assertEqual("Smith, Bob\t123456789", str(student))
