# RedBus Calendar Automation

## Description
This project automates the process of selecting a date from the RedBus website calendar using Python and Selenium.

## Author
- **Name:** Suman Gangopadhyay
- **Email:** linuxgurusuman@gmail.com
- **Date:** 25-Oct-2024
- **Version:** 1.0

## Technologies Used
- **Programming Language:** Python
- **Automation Library:** Selenium
- **Web Driver:** ChromeDriver

## Prerequisites
Ensure you have the following installed:
- Python (latest version recommended)
- Selenium
- Chrome WebDriver (managed via `webdriver_manager`)

## Installation
Follow these steps to set up the project:

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
To run the automation script, execute the following command:

```sh
python redbus_automation.py
```

## Features
- Opens the RedBus homepage.
- Clicks on the calendar element.
- Selects a specific date (e.g., 18th).
- Closes the browser after execution.

## Caveats
None identified.

## Potential Enhancements
- Add support for selecting any date dynamically.
- Implement logging and exception handling for better debugging.
- Extend automation to cover more booking steps.

## License
This project is open-source and available under the MIT License.

