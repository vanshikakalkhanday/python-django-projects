from django.test import TestCase

from django.core.exceptions import ValidationError

from .models import Student


class StudentModelTest(TestCase):

    def test_student_creation(self):

        student = Student.objects.create(

            name="John",

            age=20,

            email="john@example.com"

        )

        self.assertEqual(student.name, "John")

        self.assertEqual(student.age, 20)

        self.assertEqual(str(student), "John")

    def test_age_validator(self):

        student = Student(

            name="Invalid",

            age=150,

            email="test@example.com"

        )

        with self.assertRaises(ValidationError):

            student.full_clean()
 