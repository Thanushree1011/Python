# Python Practice and Unit Testing Assignments

This repository contains Python programming assignments focused on Python fundamentals, clean coding practices, unit testing, and test-driven development.

## Repository Structure

The work is organized into separate Git branches.

### 1. `main-python-assignment`

This branch contains five Python practice assignments:

| Assignment | Description |
|---|---|
| Database Record Generator | Uses a generator to process large numbers of MySQL records efficiently while keeping memory usage low. |
| Person Class | Implements an abstract `Person` class with `Male` and `Female` subclasses that define the `get_gender()` method. |
| Remove Duplicates | Removes duplicate elements from a list while preserving their original order. |
| Squares Using `map()` and `lambda` | Generates the squares of numbers from 1 to 20 using `map()` and a lambda function. |
| Anti-HTML | Implements the `anti_html.py` assignment. |

The assignments include relevant unit tests to verify program behavior.

### 2. `unittest-assignment`

This branch contains exercises based on Python unit testing and Test-Driven Development (TDD).

**Main components:**

- **TDD Example:** Implements string reversal, longest-word identification, list reversal, and digit counting.
- **General Example:** Implements dictionary flattening and employee-record retrieval, with tests that mock database calls.
- **DynamoDB Example:** Contains exercises for creating a DynamoDB table, adding records, and testing failure scenarios.
- **S3 Example:** Tests saving data to an Amazon S3 bucket using mocked AWS services.

The project uses `pytest` for running tests, Python's `unittest.mock` for mocking dependencies, and `moto` for simulating AWS services during tests.

## Technologies Used

- Python
- Pytest
- Python `unittest.mock`
- Boto3
- Moto
- Git and GitHub

## Running the Tests

Run these commands from the project directory after activating the appropriate virtual environment.

Run all tests:

```bash
python -m pytest -v
```

Run tests for the TDD example:

```bash
python -m pytest tests/test_tdd_example.py -v
```

Run tests for the general example:

```bash
python -m pytest tests/test_general_example.py -v
```

## Learning Objectives

- Understand Python classes, inheritance, and abstraction.
- Process data efficiently using generators.
- Apply list and dictionary operations.
- Write and execute unit tests.
- Use mocking to isolate code from external dependencies.
- Practice Test-Driven Development.
- Organize assignments using Git branches and version control.

## Repository Branches

- `main` — Repository's main branch.
- `main-python-assignment` — Python practice assignments.
- `unittest-assignment` — Unit testing and TDD exercises.

