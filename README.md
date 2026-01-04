
---

# Mini Assessment Engine (Acad AI)

A Django REST–based Mini Assessment Engine that allows students to discover exams, submit answers securely, and receive automated grading feedback for both multiple-choice and text-based questions.

This project demonstrates **clean backend architecture**, **secure API design**, and **modular automated grading logic**, in line with Acad AI’s backend test requirements.

---

## Features

* Exam discovery and retrieval
* Secure student submissions (token-based authentication)
* Support for:

  * Multiple Choice Questions (MCQs)
  * Text-based questions
* Automated grading:

  * Deterministic grading for MCQs
  * TF-IDF + cosine similarity for text answers
* One-attempt-per-exam enforcement
* Optimized database queries
* Interactive API documentation via Swagger

---

## Architecture Overview

The project follows a **domain-driven structure** within a single Django app for clarity:

```
assessment/
├── models.py        # Exam, Question, Submission, Answer
├── views.py         # API endpoints
├── services.py      # Grading logic (pure, stateless)
├── tasks.py         # Grading orchestration
├── urls.py          # API routing
└── management/
    └── commands/
        └── seed_exams.py
```

### Separation of Concerns

* **views.py** → HTTP, validation, permissions
* **tasks.py** → grading orchestration and score aggregation
* **services.py** → grading algorithms only (no Django dependencies)

This design allows the grading engine to be replaced or extended (e.g. LLM-based grading) without touching API logic.

---

##  Grading Logic

### MCQ Questions

* Exact match between student answer and expected option (`A–D`)
* Full marks or zero

### Text Questions

* Graded using **TF-IDF vectorization + cosine similarity**
* Partial credit supported
* Defensive checks prevent crashes and nonsense scoring
* Very short or empty answers receive zero

The grading strategy is selected dynamically based on question type.

---

##  Authentication

* Token-based authentication using Django REST Framework
* Each request to protected endpoints must include:

```
Authorization: Token <your_token>
```

Students can only:

* Submit exams once
* View their own submissions and results

---

## API Endpoints

### Exams

* `GET /assessment/exams/`
  List all published exams

* `GET /assessment/exams/{id}/`
  Retrieve exam details and questions (no answers exposed)

### Submissions

* `POST /assessment/exams/{id}/submit/`
  Submit answers for an exam

  Example payload:

  ```json
  {
    "answers": {
      "1": "A",
      "2": "D",
      "3": "Polymorphism allows objects..."
    }
  }
  ```

* `GET /assessment/my-submissions/`
  View authenticated user’s submissions and scores

---

## API Documentation (Swagger)

Interactive API documentation is available at:

```
/assessment/docs/
```

The Swagger UI includes:

* Authentication requirements
* Request/response examples
* Error responses

---

## Database Design

Core models:

* **Exam**
* **Question**
* **Submission**
* **Answer**


---

## Seed Data

A custom management command seeds the database with:

* 3 exams
* 10 MCQs per exam
* 3 additional text-based questions per exam

Run:

```bash
python manage.py seed_exams
```

---

## Setup Instructions

### 1. Clone & install

```bash
git clone https://github.com/rcezea/Mini-Assessment-Engine
cd Mini-Assessment-Engine
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Migrate

```bash
python manage.py migrate
```

### 3. Seed data

```bash
python manage.py seed_exams
```

### 4. Run server

```bash
python manage.py runserver
```

---

## Testing the Flow

1. Create a user (admin or shell)
2. Generate a token
3. Use Swagger or Postman to:

   * List exams
   * Fetch questions
   * Submit answers
   * View results

---
