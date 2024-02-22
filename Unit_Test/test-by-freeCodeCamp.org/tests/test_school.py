import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents

@pytest.fixture
def frodo_classroom():
    teacher = Teacher("Gandalf")
    students = [Student("Sam"), Student("Merry"), Student("Pippin")]
    course_title = "Journey to Mordor"
    return Classroom(teacher, students, course_title)

def test_add_student(frodo_classroom):
    frodo_classroom.add_student(Student("Frodo"))
    assert len(frodo_classroom.students) == 4

def test_add_too_many_students(frodo_classroom):
    with pytest.raises(TooManyStudents):
        for i in range(10):
            frodo_classroom.add_student(Student(f"Student_{i}"))

def test_remove_student(frodo_classroom):
    frodo_classroom.remove_student("Merry")
    assert len(frodo_classroom.students) == 2
    assert all(student.name != "Merry" for student in frodo_classroom.students)

def test_change_teacher(frodo_classroom):
    frodo_classroom.change_teacher(Teacher("Aragorn"))
    assert frodo_classroom.teacher.name == "Aragorn"
