import os
from models import Person
from dotenv import load_dotenv
from google import genai
from models import Classification, SCHEMA_MAP
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options={"timeout": 60.0}
)

user_input = """
Student Profile:
Name: Ananya Sharma
Roll Number: CS-2023-088
Department: Computer Science and Engineering
Currently enrolled in 3rd Year.
Registered Courses: Data Structures, Operating Systems, Computer Networks.
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=f"""
    Classify the following input into exactly one of
    these categories:

    - resume
    - invoice
    - student

    Input:
    {user_input}
    """,
    config={
        "response_mime_type": "application/json",
        "response_schema": Classification,
    }
)

classification = Classification.model_validate_json(
    response.text
)

print(classification.document_type)
selected_schema = SCHEMA_MAP[
    classification.document_type
]

res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
    Extract the information from the following input.

    Only extract information that is actually present.
    Do not invent information.

    Input:
    {user_input}
    """,
    config={
        "response_mime_type": "application/json",
        "response_schema": selected_schema,
    }
)
print(res)
result = selected_schema.model_validate_json(
    res.text
)
print(result)

