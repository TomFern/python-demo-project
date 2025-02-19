# Demo Project for Python and CI/CD

This is a demo Python project designed to showcase a CI/CD pipeline for Python projects. It includes:

- **Unit tests** with pytest.
- **Integration tests**.
- **Linting** with flake8 (see the `lint` target in the Makefile).
- A **build step** to package the project.

## Getting Started

It's recommended to create a virtualenv first:

```bash
python3 -m venv venv
source venv/bin/activate
```

1. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. Run tests:

    ```bash
    make test
    ```

    ```bash
    make lint
    ```

3. Build a release wheel:

    ```bash
    make build
    ```

## Project structure

```text
ci_cd_demo_project/
├── .gitignore
├── Makefile
├── README.md
├── requirements.txt
├── setup.py
├── demo_project
│   ├── __init__.py
│   └── calculator.py
└── tests
    ├── __init__.py
    ├── test_calculator_integration.py
    └── test_calculator_unit.py
```


