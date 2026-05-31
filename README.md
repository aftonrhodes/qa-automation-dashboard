[![Python application](https://github.com/aftonrhodes/qa-automation-dashboard/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/aftonrhodes/qa-automation-dashboard/actions/workflows/python-app.yml)

# E2E Playwright Test Suite

A robust end-to-end (E2E) testing framework designed to validate cloud-hosted dashboard applications. This project demonstrates automated UI testing using Playwright and Python, with a production-grade CI/CD pipeline that includes automated daily regression testing to ensure continuous application health and reliability.

## Highlights
* **Automated UI Testing:** Validates dashboard loading and critical UI elements.
* **CI/CD Integration:** Uses GitHub Actions for automated regression testing on every push.
* **Cloud-Native:** Infrastructure provisioned and hosted via AWS S3.
* **Best Practices:** Implements isolated virtual environments, secure credential handling, and automated build reporting.

## Tech Stack
* **Language:** Python 3.10+
* **Testing Framework:** Playwright & Pytest
* **CI/CD:** GitHub Actions
* **Cloud Infrastructure:** AWS S3

## Installation & Setup
To run this project locally, ensure you have Python installed, then follow these steps:

### Set up virtual environment:

python3 -m venv venv
source venv/bin/activate

### Install dependencies:

pip install playwright pytest-playwright
playwright install chromium

### Run the tests:

pytest test_dashboard.py