# Exercise Pytest + Playwright

This exercise to perform end to end testing with Pytest and Playwright.

## Getting started

To install the requirements do:

```
pip install -r requirements.txt
```

## Project folder structure

```
- allure_results        # report files
- projects              # parent folder
  |
   - backend            # backend project
     |
      - consumers       # containing all consumers
      - core            # containing core classes
      - objects         # containing backend objects
      - schemas         # containing schemas for testing
      - tests           # containing the actual pytest tests
   - frontend           # frontend project
     |
      - core            # containing core classes
      - tests           # containing the actual pytest tests
   - performance        # performance project
     |
      - locustfiles     # containing the performance tests
   - shared             # shared between projects
- .env                  # .env file to contain environmental or sensitive information
- .gitignore
- conftest.py           # conftest file for pytest
- pyproject.toml        # project setup file
- requirements.txt      # pip requirements
```
