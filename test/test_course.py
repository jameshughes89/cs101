from unittest import TestCase

from src.course import Course
from src.student import Student


class CourseTest(TestCase):
    def test_course_name_returns_correct_name(self):
        course = Course("CS101")
        self.assertEqual("CS101", course.course_name)

    def test_size_empty_course_returns_0(self):
        course = Course("CS101")
        self.assertEqual(0, course.size())

    def test_find_empty_course_returns_negative_1(self):
        course = Course("CS101")
        student = Student("Bob", "Smith", 123456789)
        self.assertEqual(-1, course._find(student))

    def test_remove_empty_course_raises_value_error(self):
        course = Course("CS101")
        student = Student("Bob", "Smith", 123456789)
        with self.assertRaises(ValueError):
            course.remove(student)
            
    def test_contains_empty_course_returns_false(self):
        course = Course("CS101")
        student_not_there = Student("Not", "There", 918273645)
        self.assertFalse(course.contains(student_not_there))

    def test_repr_empty_course_returns_empty_string(self):
        course = Course("CS101")
        self.assertEqual("", str(course))

    def test_size_singleton_returns_1(self):
        course = Course("CS101")
        student = Student("Bob", "Smith", 123456789)
        course.add(student)
        self.assertEqual(1, course.size())

    def test_find_singleton_student_does_not_exist_returns_negative_1(self):
        course = Course("CS101")
        student = Student("Bob", "Smith", 123456789)
        course.add(student)
        student_not_there = Student("Not", "Bob", 987654321)
        self.assertEqual(-1, course._find(student_not_there))

    def test_find_singleton_student_exists_returns_correct_index(self):
        course = Course("CS101")
        student = Student("Bob", "Smith", 123456789)
        course.add(student)
        student_there = Student("Bob", "Smith", 123456789)
        self.assertEqual(0, course._find(student_there))

    def test_contains_singleton_student_does_not_exist_returns_false(self):
        course = Course("CS101")
        student = Student("Bob", "Smith", 123456789)
        course.add(student)
        student_not_there = Student("Not", "Bob", 987654321)
        self.assertFalse(course.contains(student_not_there))

    def test_contains_singleton_student_exists_returns_true(self):
        course = Course("CS101")
        student = Student("Bob", "Smith", 123456789)
        course.add(student)
        student_there = Student("Bob", "Smith", 123456789)
        self.assertTrue(course.contains(student_there))

    def test_remove_singleton_student_does_not_exist_raises_value_error(self):
        course = Course("CS101")
        student = Student("Bob", "Smith", 123456789)
        course.add(student)
        student_not_there = Student("Not", "Bob", 987654321)
        with self.assertRaises(ValueError):
            course.remove(student_not_there)

    def test_remove_singleton_student_exists_removes_student(self):
        course = Course("CS101")
        student = Student("Bob", "Smith", 123456789)
        course.add(student)
        course.remove(student)
        self.assertEqual(-1, course._find(student))

    def test_repr_singleton_returns_correct_string(self):
        course = Course("CS101")
        student = Student("Bob", "Smith", 123456789)
        course.add(student)
        expected = "Smith, Bob\t123456789\n"
        self.assertEqual(expected, str(course))

    def test_size_many_students_returns_correct_size(self):
        course = Course("CS101")
        course.add(Student("Bob", "Smith", 123456789))
        course.add(Student("Jane", "Doe", 987654321))
        course.add(Student("Niles", "MacDonald", 192837465))
        self.assertEqual(3, course.size())

    def test_find_many_students_student_does_not_exist_returns_negative_1(self):
        course = Course("CS101")
        course.add(Student("Bob", "Smith", 123456789))
        course.add(Student("Jane", "Doe", 987654321))
        course.add(Student("Niles", "MacDonald", 192837465))
        student_not_there = Student("Not", "There", 918273645)
        self.assertEqual(-1, course._find(student_not_there))

    def test_find_many_students_student_exists_returns_correct_index(self):
        course = Course("CS101")
        course.add(Student("Bob", "Smith", 123456789))
        course.add(Student("Jane", "Doe", 987654321))
        course.add(Student("Niles", "MacDonald", 192837465))
        student_there = Student("Jane", "Doe", 987654321)
        self.assertEqual(1, course._find(student_there))

    def test_find_many_students_duplicate_students_returns_first_occurrence_index(self):
        course = Course("CS101")
        course.add(Student("Bob", "Smith", 123456789))
        course.add(Student("Jane", "Doe", 987654321))
        course.add(Student("Niles", "MacDonald", 192837465))
        course.add(Student("Jane", "Doe", 987654321))
        student_there = Student("Jane", "Doe", 987654321)
        self.assertEqual(1, course._find(student_there))

    def test_contains_many_students_student_does_not_exist_returns_false(self):
        course = Course("CS101")
        course.add(Student("Bob", "Smith", 123456789))
        course.add(Student("Jane", "Doe", 987654321))
        course.add(Student("Niles", "MacDonald", 192837465))
        student_not_there = Student("Not", "There", 918273645)
        self.assertFalse(course.contains(student_not_there))


    def test_contains_many_students_student_exists_returns_true(self):
        course = Course("CS101")
        course.add(Student("Bob", "Smith", 123456789))
        course.add(Student("Jane", "Doe", 987654321))
        course.add(Student("Niles", "MacDonald", 192837465))
        student_there = Student("Jane", "Doe", 987654321)
        self.assertTrue(course.contains(student_there))

    def test_contains_many_students_duplicate_students_returns_true(self):
        course = Course("CS101")
        course.add(Student("Bob", "Smith", 123456789))
        course.add(Student("Jane", "Doe", 987654321))
        course.add(Student("Niles", "MacDonald", 192837465))
        course.add(Student("Jane", "Doe", 987654321))
        student_there = Student("Jane", "Doe", 987654321)
        self.assertTrue(course.contains(student_there))

    def test_remove_many_students_student_does_not_exist_raises_value_error(self):
        course = Course("CS101")
        course.add(Student("Bob", "Smith", 123456789))
        course.add(Student("Jane", "Doe", 987654321))
        course.add(Student("Niles", "MacDonald", 192837465))
        student_not_there = Student("Not", "There", 918273645)
        with self.assertRaises(ValueError):
            course.remove(student_not_there)

    def test_remove_many_students_student_exists_removes_student(self):
        course = Course("CS101")
        course.add(Student("Bob", "Smith", 123456789))
        course.add(Student("Jane", "Doe", 987654321))
        course.add(Student("Niles", "MacDonald", 192837465))
        student_there = Student("Jane", "Doe", 987654321)
        course.remove(student_there)
        self.assertEqual(-1, course._find(student_there))

    def test_remove_many_students_duplicate_students_removes_first_occurrence(self):
        course = Course("CS101")
        course.add(Student("Bob", "Smith", 123456789))
        course.add(Student("Jane", "Doe", 987654321))
        course.add(Student("Niles", "MacDonald", 192837465))
        course.add(Student("Jane", "Doe", 987654321))
        student_there = Student("Jane", "Doe", 987654321)
        course.remove(student_there)
        self.assertEqual(2, course._find(student_there))

    def test_repr_many_student_returns_correct_string(self):
        course = Course("CS101")
        course.add(Student("Bob", "Smith", 123456789))
        course.add(Student("Jane", "Doe", 987654321))
        course.add(Student("Niles", "MacDonald", 192837465))
        expected = "Smith, Bob\t123456789\n" "Doe, Jane\t987654321\n" "MacDonald, Niles\t192837465\n"
        self.assertEqual(expected, str(course))
