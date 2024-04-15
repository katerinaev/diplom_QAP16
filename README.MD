# Python QA Automation Project

## Description
This project is focused on automating tests for the Frontline Education website using Selenium WebDriver in Python. It aims to provide automated testing for various functionalities and elements of the website to ensure its reliability and functionality.

## Installation
1. Clone the repository from GitHub to your local machine.
2. Ensure Python is installed on your system.
3. Install project dependencies: `pip install -r requirements.txt`
4. Set up WebDriver according to your browser (e.g., ChromeDriver for Chrome)

## Run tests
- Run the tests using the command `pytest` in 
- Run tests through allure `python -m pytest --alluredir=allure-results`
- Generate and open Allure-report to view the test results: `allure serve allure-results`
- Check the project on PEP8 `flake8 --exclude=venv --count --max-line-length=120 -v`

## Project structure:

* `data\` - data for tests (URLs)
* `elements\` - modules for interacting with specific elements on the website (header, footer, bot)
* `helpers\` - directory with the BasePage
* `pages\` - description of actions with pages, elements and their locators
* `tests\` - directory with all autotests
* `conftest.py` - fixtures for running tests
* `requirements.txt` - list of dependencies used in this project

## Test cases
https://docs.google.com/spreadsheets/d/1NqGWJ66MgART1r8zRS13mtzjzWZwPdiVNBkcJIwyH-Y/edit?usp=sharing