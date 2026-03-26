# OrangeHRM UI Automation Framework

## 🔹 Project Overview

This project is a UI automation framework built using Selenium with Python for the OrangeHRM application.

## 🔹 Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* Git & GitHub
* GitHub Actions (CI/CD)

## 🔹 Features Implemented

* Login functionality automation
* PIM module navigation
* Add Employee functionality
* Smoke and regression test coverage
* JSON-based test data handling
* Explicit wait handling for stability
* CI pipeline using GitHub Actions

## 🔹 Framework Highlights

* Modular Page Object Model design
* Reusable utility functions (WaitUtils, path handling)
* CI-friendly and headless execution support
* Clean separation of test and page logic

## 🔹 How to Run Tests

```bash
Run smoke tests: pytest -m smoke
Run regression tests: pytest -m regression
Run sanity tests: pytest -m sanity
Run all tests:pytest
```

## 🔹 CI/CD

Integrated with GitHub Actions for automated test execution on every push and pull request.

## 🔹 Future Enhancements

* Employee List validation
* Advanced form validations
* API integration
