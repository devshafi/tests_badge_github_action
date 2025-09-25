# Simple Flask Calculator App

![Tests](https://github.com/devshafi/tests_badge_github_action/actions/workflows/test.yml/badge.svg)
[![codecov](https://codecov.io/gh/devshafi/tests_badge_github_action/branch/main/graph/badge.svg)](https://codecov.io/gh/devshafi/tests_badge_github_action)

A simple Flask application that provides a REST API for basic calculator operations.

## Features

- ✅ Addition
- ✅ Subtraction
- ✅ Multiplication
- ✅ Division (with zero-division error handling)
- ✅ Power/Exponentiation
- ✅ Comprehensive unit tests
- ✅ GitHub Actions CI/CD
- ✅ Code coverage reporting

## API Endpoints

- `GET /` - API documentation
- `POST /add` - Add two numbers
- `POST /subtract` - Subtract two numbers
- `POST /multiply` - Multiply two numbers
- `POST /divide` - Divide two numbers
- `POST /power` - Raise first number to power of second

### Request Format

All POST endpoints expect JSON data with parameters `a` and `b`:

```json
{
  "a": 10,
  "b": 5
}
```

### Response Format

Success response:
```json
{
  "result": 15
}
```

Error response:
```json
{
  "error": "Error message"
}
```

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The app will be available at `http://localhost:5000`

## Testing

Run the tests with coverage:

```bash
pytest --cov=. --cov-report=html tests/
```

This will generate an HTML coverage report in the `htmlcov/` directory.

## GitHub Actions

The repository includes a GitHub Actions workflow that:
- Runs tests on every push and pull request
- Generates coverage reports
- Uploads coverage to Codecov
- Creates test status and coverage badges

## Project Structure

```
.
├── app.py              # Flask application
├── calculator.py       # Calculator functions
├── requirements.txt    # Python dependencies
├── tests/
│   ├── __init__.py
│   └── test_calculator.py  # Unit tests
├── .github/
│   └── workflows/
│       └── test.yml    # GitHub Actions workflow
└── README.md           # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Ensure all tests pass
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).