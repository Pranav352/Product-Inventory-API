![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-4.x-green)
![Tests](https://img.shields.io/badge/tests-pytest-orange)

# Product Inventory API

A RESTful API built with **Python**, **Django**, and **Django REST Framework** for managing product inventory.
This project demonstrates best practices in backend development including API design, automated testing, code quality checks, and CI integration.

---

## Features

* CRUD operations for product management
* JWT Authentication
* API documentation using Swagger
* Automated testing with Pytest
* Code linting and formatting
* Static type checking
* Pre-commit hooks for code quality
* Continuous Integration support

---

## Tech Stack

* Python
* Django
* Django REST Framework
* Pytest
* Ruff (Linting & formatting)
* Pyright (Type checking)
* Pre-commit (Git hooks)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/product-inventory-api.git
cd product-inventory-api
```

Create and activate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start development server:

```bash
python manage.py runserver
```

---

## API Endpoints

| Method | Endpoint                | Description          |
| ------ | ----------------------- | -------------------- |
| GET    | `/api/v1/products`      | List all products    |
| POST   | `/api/v1/products`      | Create a new product |
| GET    | `/api/v1/products/{id}` | Retrieve a product   |
| PUT    | `/api/v1/products/{id}` | Update a product     |
| DELETE | `/api/v1/products/{id}` | Delete a product     |

---
API Documentation Links

 using Swagger in Django REST Framework:

| Documentation | URL |
|------|------|
| Swagger UI | http://127.0.0.1:8000/swagger/ |
| ReDoc | http://127.0.0.1:8000/redoc/ |

## Useful Tool Links

references to  tools used in project:

## Tools Used

- Ruff – https://docs.astral.sh/ruff/
- Pyright – https://github.com/microsoft/pyright
- Pytest – https://docs.pytest.org/


## Running Tests

Run all tests using:

```bash
pytest
```

Generate coverage report:

```bash
pytest --cov
```

---
![Ruff](https://img.shields.io/badge/lint-ruff-blue)
![Pyright](https://img.shields.io/badge/type%20check-pyright-yellow)
![Pytest](https://img.shields.io/badge/tests-pytest-green)
## Code Quality  

This project enforces strict code quality standards.

| Tool       | Purpose                           |
| ---------- | --------------------------------- |
| Ruff       | Python linting and formatting     |
| Pyright    | Static type checking              |
| Pytest     | Automated testing                 |
| Pre-commit | Run checks before committing code |

---

## Project Structure

```text
product-inventory-api/
│
├── inventory_api/           # Django project configuration
├── products/                # Product app
├── tests/                   # Automated tests
│
├── .github/
│   └── workflows/
│       └── ci.yml           # CI pipeline
│
├── .pre-commit-config.yaml
├── .flake8
├── pyproject.toml
├── pytest.ini
├── requirements.txt
├── .gitignore
├── README.md
└── manage.py
```

---

## API Documentation Links

using Swagger in Django REST Framework:

| Documentation | URL |
|------|------|
| Swagger UI | http://127.0.0.1:8000/swagger/ |
| ReDoc | http://127.0.0.1:8000/redoc/ |

---

## Continuous Integration

This project includes a CI pipeline that runs:

* Lint checks
* Type checking
* Automated tests

on every push and pull request.

---
Issues & Contributions

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

Issues: https://github.com/Pranav352/product-inventory-api/issues

## Professional README Links Section

You can add this section:

## Useful Links

- Repository: https://github.com/Pranav352/product-inventory-api
- API Docs: http://127.0.0.1:8000/swagger/
- Issues: https://github.com/Pranav352/product-inventory-api/issues

![License](https://img.shields.io/badge/license-MIT-blue)
## License 

This project is licensed under the MIT License.
![Visitors](https://img.shields.io/badge/Visitors-1000-blue)
![GitHub Stars](https://img.shields.io/github/stars/Pranav352/portfolio-website?style=social)




