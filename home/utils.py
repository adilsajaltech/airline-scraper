from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def get_cookies():
    # Launch the browser
    driver = webdriver.Chrome()  # Or any other webdriver (e.g., Firefox, Edge, etc.)

    # Visit the website
    driver.get('https://www.swiss.com/lhg/gb/en/o-d/cy-cy/london-gb-frankfurt')

    # Wait for the accept button to be clickable
    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="cm-acceptAll"]'))
    )

    # Click the accept button
    accept_button.click()

    # Wait for a moment
    time.sleep(2)


    # Scroll to the calendar button
    calender_button = driver.find_element(By.CLASS_NAME, 'form-group.calendar-input')
    driver.execute_script("arguments[0].scrollIntoView();", calender_button)
    time.sleep(1)

    # Click the calendar button
    calender_button.click()
    time.sleep(2)



    # Wait for the first button to be clickable
    oneway_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'checkbox-like'))
    )

    # Click the first button
    oneway_button.click()
    time.sleep(1)


    # Wait for the button to be clickable
    date_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//td[@tabindex="-1" and @data-date="2024-04-27"]'))
    )

    # Click the button
    date_button.click()


    time.sleep(2)



    # Wait for the first button to be clickable
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'calendar-footer-continue-button'))
    )

    # Click the first button
    continue_button.click()
    time.sleep(1)



    # Wait for the first button to be clickable
    flight_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'searchFlights'))
    )

    # Click the first button
    flight_button.click()
    time.sleep(35)





    cookies = driver.get_cookies()


    # # Wait for a moment
    time.sleep(2)

    # Close the browser
    driver.quit()
    
    return cookies




def format_cookies(cookies):
    formatted_cookies = []
    for cookie in cookies:
        formatted_cookie = f"{cookie['name']}={cookie['value']}"
        formatted_cookies.append(formatted_cookie)
    return "; ".join(formatted_cookies)