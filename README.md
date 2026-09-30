# Structured Output Agent with Gemini & Pydantic

An intelligent two-stage extraction agent built with **Google Gemini (google-genai)** and **Pydantic**. 

It automatically classifies unstructured text input into a specific document category, dynamically selects the corresponding Pydantic schema from a registry, and extracts strongly typed, validated JSON data.

---

## Architecture Flow

```
Unstructured Input Text
          │
          ▼
┌──────────────────┐
│  Stage 1:        │  Uses `Classification` schema
│  Classification  │  (resume | invoice | student)
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│  Schema Registry │  Matches category to Pydantic Model
│  (`SCHEMA_MAP`)  │  via dynamic lookup
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│  Stage 2:        │  Enforces `response_schema`
│  Extraction      │  with Gemini Structured Output
└─────────┬────────┘
          │
          ▼
Typed & Validated Pydantic Object
```

---

## Features

- **Dynamic Schema Routing**: Classifies raw input text and automatically routes it to the appropriate data contract.
- **Strict Structured Outputs**: Utilizes Gemini's native `response_schema` and `response_mime_type="application/json"` guarantees.
- **Type Safety & Validation**: Validates output directly into Pydantic models (`Student`, `Resume`, `Invoice`, `Person`).
- **Zero Hallucination Guard**: Extraction prompts instruct the model to only extract information explicitly present in the input.

---

## Project Structure

```text
├── models.py          # Pydantic schemas (Classification, Resume, Invoice, Student, Person) & SCHEMA_MAP
├── main.py            # Agent pipeline (Classification -> Dynamic Extraction -> Validation)
├── requirements.txt   # Dependencies

```

---

## Schemas Defined

| Category | Model | Extracted Fields |
| :--- | :--- | :--- |
| `resume` | `Resume` | `name`, `role`, `skills`, `education`, `experience` |
| `invoice` | `Invoice` | `invoice_number`, `vendor`, `date`, `total_amount`, `currency` |
| `student` | `Student` | `name`, `roll_number`, `branch`, `year`, `subjects` |
| `Person` | `Person` | `name`, `age`, `skills` |

---

## Getting Started

### 1. Prerequisites
- Python 3.10+
- A Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/)

### 2. Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/Manvita22/structuredoutput.git
cd structuredoutput

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

Install dependencies:

```bash
pip install google-genai pydantic python-dotenv
```

### 3. Environment Setup

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Running the Agent

Run the main execution script:

```bash
python main.py
```

---

## Example Usage

### Input
```python
user_input = """
Student Profile:
Name: Ananya Sharma
Roll Number: CS-2023-088
Department: Computer Science and Engineering
Currently enrolled in 3rd Year.
Registered Courses: Data Structures, Operating Systems, Computer Networks.
"""
```

### Output
```json
{
  "name": "Ananya Sharma",
  "roll_number": "CS-2023-088",
  "branch": "Computer Science and Engineering",
  "year": 3,
  "subjects": ["Data Structures", "Operating Systems", "Computer Networks"]
}
```
