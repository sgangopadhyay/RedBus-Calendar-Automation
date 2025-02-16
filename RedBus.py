"""
Program Description : RedBus Calendar Automation using Python Selenium
Programmer : Suman Gangopadhyay
Email ID : linuxgurusuman@gmail.com
Date : 25-Oct-2024
Version : 1.0
Code Library : Selenium
Prerequisites : Python, Selenium, ChromeDriver
Caveats : None
"""

# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ERROR_URL
from time import sleep

# Data class to store URLs or other configuration data
class Data:
    # RedBus homepage URL
    url = "https://www.redbus.in/"

# Locators class to store XPaths or other locators for web elements
class Locators:
    # Locator for the calendar element
    calendar_locator = "//div[@id='onwardCal']/div/div/text[@class='dateText']"
    
    # Locator for selecting a specific date (e.g., 18th) in the calendar
    date_locator = "//div[@class='sc-jzJRlG hrJoeL']/div/div/div[3]/div[@class='DayTilesWrapper__RowWrap-sc-19pz9i8-1 fGGTDM']/span/div/span[text()='18']"

# RedBusAutomation class to handle the automation process
class RedBusAutomation(Data, Locators):
    def __init__(self):
        # Initialize the Chrome WebDriver using ChromeDriverManager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def startup(self):
        """
        Start the browser, maximize the window, and navigate to the RedBus homepage.
        """
        try:
            self.driver.maximize_window()  # Maximize the browser window
            self.driver.get(self.url)  # Open the RedBus homepage
            self.driver.implicitly_wait(10)  # Wait for elements to load (up to 10 seconds)
        except ERROR_URL as error:
            return error  # Return any URL-related errors

    def shutdown(self):
        """
        Close the browser and end the WebDriver session.
        """
        self.driver.quit()

    def automation(self):
        """
        Automate the process of selecting a date from the calendar.
        """
        try:
            # Click on the calendar element to open the date picker
            self.driver.find_element(by=By.XPATH, value=self.calendar_locator).click()
            
            # Select the specific date (e.g., 18th) from the calendar
            self.driver.find_element(by=By.XPATH, value=self.date_locator).click()
            
            sleep(2)  # Wait for 2 seconds to observe the action
        except NoSuchElementException as error:
            return error  # Return any element-not-found errors
        finally:
            self.shutdown()  # Ensure the browser is closed after execution

# Main execution block
if __name__ == "__main__":
    # Create an instance of the RedBusAutomation class
    suman = RedBusAutomation()

    # Start the browser and navigate to the RedBus homepage
    suman.startup()

    # Perform the automation task (selecting a date from the calendar)
    suman.automation()
