from unittest import TestCase, main
from project.student import Student

class StudentTests(TestCase):
    def setUp(self):
        self.student = Student("test", {"Advanced": ['will pass', 'yes']})

    def test_init_if_courses_is_none(self):
        student = Student("test")

        self.assertEqual("test", student.name)
        self.assertEqual({}, student.courses)

    def test_init(self):
        self.assertEqual("test", self.student.name)
        self.assertEqual({"Advanced": ['will pass', 'yes']}, self.student.courses)

    def test_enroll_if_course_name_exists(self):
        result = self.student.enroll("Advanced", ['new_note'])
        self.assertEqual({"Advanced": ['will pass', 'yes', 'new_note']}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_if_add_course_notes(self):
        result = self.student.enroll("Basic", ['new_note'])
        self.assertEqual({"Advanced": ['will pass', 'yes'], "Basic": ['new_note']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

        result = self.student.enroll("Fund", ['test_note'], "Y")
        self.assertEqual({"Advanced": ['will pass', 'yes'], "Basic": ['new_note'], "Fund": ['test_note']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_new_course_and_not_add_course_notes(self):
        result = self.student.enroll("Basic", ['new_note'], 'N')
        self.assertEqual({"Advanced": ['will pass', 'yes'], "Basic": []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_course_name_exists(self):
        result = self.student.add_notes("Advanced", 'new_note')

        self.assertEqual({"Advanced": ['will pass', 'yes', 'new_note']}, self.student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_course_name_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Basic", 'new_note')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({"Advanced": ['will pass', 'yes']}, self.student.courses)

    def leave_course_course_name_exists(self):
        result = self.student.leave_course("Advanced")

        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_name_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Basic")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual({"Advanced": ['will pass', 'yes']}, self.student.courses)


if __name__ == '__main__':
    main()