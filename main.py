from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Structure of data
class Student(BaseModel):
    id: int
    name: str
    degree: str 

students: List[Student] = []

# Decorator : gives super power to functions

@app.get("/")  # Home page
def read_root():
    return {"message":"Welcome to student portal"}

@app.get("/students")  # get all students list
def get_students():
    return students

@app.post("/students")  # Add new student
def add_students(student: Student):
    students.append(student)
    return student

@app.put("/students/{student_id}")  # Update student
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return {"message":"Student updated successfully!!"}
    return {"error":"Student not found"}

@app.delete("/students/{studnet_id}")  # Delete student
def delete_student(student_id:int):
    for index, student in enumerate(students):
        if student.id == student_id:
            deleted = students.pop(index)
            return deleted
    return {"error":"Student not found"}
