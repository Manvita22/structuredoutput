from pydantic import BaseModel
from typing import Literal

class Person(BaseModel):
    name: str
    age: int
    skills: list[str]

class Resume(BaseModel):
    name: str | None = None
    role: str | None = None
    skills: list[str] = []
    education: list[str] = []
    experience: list[str] = []


class Invoice(BaseModel):
    invoice_number: str | None = None
    vendor: str | None = None
    date: str | None = None
    total_amount: float | None = None
    currency: str | None = None


class Student(BaseModel):
    name: str | None = None
    roll_number: str | None = None
    branch: str | None = None
    year: int | None = None
    subjects: list[str] = []

class Classification(BaseModel):
    document_type: Literal[
        "Person",
        "resume",
        "invoice",
        "student"
    ]

#schema registry
SCHEMA_MAP = {
    "resume": Resume,
    "invoice": Invoice,
    "student": Student
}