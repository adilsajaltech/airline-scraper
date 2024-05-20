import requests

def get_token():

    url = "https://api-shop.swiss.com/v1/oauth2/token"

    payload = {
        "client_id": "8reubuqz8gkn2vs3wbenb4zg",
        "client_secret": "FTaj$p54j",
        "fact": '{"keyValuePairs":[{"key":"country","value":"DE"}]}',
        "grant_type": "client_credentials"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://shop.swiss.com",
        "Referer": "https://shop.swiss.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Akamai-Bm-Telemetry": "a=3635805540034FFCDE6C800F12C8C166&&&e=ODM0MzExRTAxMjYwNERGRTQyREI2OUVGMzQ2MzRDMTZ+WUFBUXp5RVBGL0VEcE0rT0FRQUFoR3BQRkJjOVRncDNMcVdtbXRua2k3QTE5L0tZejh5eHByVjJ3cVltZDlTVWEwQi9UUldaczlsNkVBUCtNUldNZ3pMTXFNMVR5MFJvNEI2VTV3aUJJUm5Gd2tnbW14enFNaFBVdHNxUm9MM3RTWjNPYTQxZ0VHVHlxRFZZYVV1ZTkwTWV5OVN3WnRtcEVZbUxibG5sRXlJMGVtQmxKQzVGVy9DMytFU3k1V21hZERDTlFhbUh4OFpCeXphNjZSNkNncWtlN2hSMEFTamRIVkpFaXlURXAvVzdOcXMrNHJ4dzVZd09IRzRDMk5HeTYxbkE0YjlaOVNIRS94ZEpleURSci9wOVllVTZLZEFPWm5QZTBuZzlLSm94NW1ITHNUdWNJcDExRUJqellLKzVnSHhpR2k1cEV5QlVFMXkxcDVtQ2tKdnJ1cmd5K2FZSWhiNzRHWC9vdFdKNDR2VkhZUFZaZFNnc0NtUjNDYS9NTW5oc3dGaURDa0dVaWJYbThXcGVyZ1RqVUVUSWg1bmp5U0hrdWtOR2VsRT1+MzE2MDM3MX4zNDg2MDIy&&&sensor_data=MjszMTYwMzcxOzM0ODYwMjI7NCwzMiwxLDAsMiw2MjtCMnloTyNxN1pKSnBnMChvcTR7OjsqJW84bmZjLktDbWdQVkYzYSMpW0M/ekNDfi9ZS2BZNHd3VCVfTVQtSHEsMmh3ZmRENFR9PDRsTj5gP1libyorPTM0Z0NBRG1KPTgvfEJNUEhHK2JCIW8vMypGT3J8P0xkZVo3eyQwb3A4MyN+QDVCKXdMdHFkN3FNe01DcXhYYHJ7LFtOT25GK3deYlZGNERyQn5OY3tSNi9fJigtUyxhKik0LGJ5a1hYKHlrcyssVE08fHV8PzFzLjFYeUxmRVdfZWs4bzJdPCgoYFZoZ004RjkodjRUTztPZjRFfkUoRHYsNy59U2UyUHFXSTdbXnwmLll9SV1fTDkqam9KRkJ3NUtmT3xQdGNEXjp+Mk9xQUVtLy55Z2BWcjthX08vOlpFP193eT1dI0ZZbDE1eixDbTZNVHdZVl18JmhbTDNrRltqdyQ2MGluWFQ8e3dTdk5edSF+WT01LXQzJVI1I2tFMll+ITVqTFZJRTlwIWApPylRP1UxdiYpUytyU08le1BFckJMXjssLDJWdVQkYTpyJlNqdFkxJmA5NVoqO29NZWZxUG99YEVgbDZmQ3ZUK24+a3Iqa19+JGdNLnR3cX1UQnZbezl9byNEbD53VE1+ZjE1JEt8bDZKNGppTFlAJk5Xc114N0AwOFkrYUdYKXFJc1pkLCh8OmRFeyN6JSUtIyllRXA8LjROb0l7SVtkJCFkNWEqJSFCYWY3PjZOVFMzRH1waiYhJFhsXT8jTnxvVy94QHZkZjdhXkFPTVtneXoydnA0dnZ3Q3FSPUokJX15UURmSExOLFJZS0tUeE9ERmdNdXhIeztwXTU6dTc+KSxxcl8+VE5aZUs0aGZVQmtmRndrdjxXY1ZORSArJmg4TiB+YDlPWDd2IG85QHB9PVllbXxXMFNYRXZzdXVqLC0vMDNsQWJuWz9MVHV+T3AwTXBxfV1QbiRuP0c4Tlp1IC8oJGNWazR5XnZ3RGEzS35BY2Z9dllROS9kdmsjN1RXdXItVkxxMi1zITpkemIhYCM/W21oWnpKOn0kN0MsLURFVWFMNG44KXhAQnxHJEEvVy8vX1dCeE0pJUUyYXpDXyt7RjwxTX18bDNPKVdDbkt9VXE1LzBaWjE6OURyfTV6U09kalpnQzlrKEMgYU95bTZ1NVheXkBucXUsNHcxZylYaTMqNWs+dlApMHckRzNmSzdSLiE6cUNYTHcxPzV+I2gkREJTJnN2JldyaEk5TXpgL1tCRk82eXwqUXtJJGMmciZKZzcockVLVFlYJHxvZUY8aD1Ra04wRk0qRCgvKl01XlRXZTshQU9Sals6QDBKaGQ8QShWOStCVyt0KXtULnMzdSlRMjBXI248PjA3Jil7a0omWnBdSnYsZSwuXUoydkxUQWxLI1NkeVFTdmBbTU9VLiQ5altXcyh1SDN8d1NHfGIoR0E4WVd+b1glcX17cXlvWiNGP0RuKnVNSDIrdnFHNFlyc3pOeHFbbnB5bj8xQS97Vi0tJGN7a1BQLDx+JnJlL2ZsYEJtUEN0VHY5TFhaS01iRV1OW2lkVSp6RU9CdHRJVTt6IUJSNUshJl9ZWGw+c3lUeyl3bDdLN052PW1TKSxUfWNeOC88PWlmVFBvKzNxMltuVi0uYnRAKlQ6PGZ1cUw/ZSljSU1QQE9LU2VnN2FMc0N8S0MtLWtSIDFLd09ZRmQ5WnZ2b0E5Lmh1TU5NZ2pQQkNEVWhqeXg0YCldJV5WRTxsQH5HeEByIz49PjpSRFg+QFcjMiFtN20pfCtILnpKa3ptZSZ6e3pUKVI+OU1HUFAkT297UWBQPShFcSxdV00+a21LSUdeITE2V3Q4TWxFNj17Qig3K1l7QiBvdG1LYVlbOUFSRz8rNVd0PHRHLX1TQFk7RV9CeWM9fCZmRV5CNHoqXlBAX0ZYQjIkezZnTTI4SClKUWgzKEN0SX1uXjYpSXtgOXVET00sQS4sJVJhS2V8PXk5byhlfG5xWE4pTyo/WEd6Tn5IJjM+dSk2dF8xSzlfN0djcCYjQ3JMU09KMm9fPikgcWRRQEptOHw/L2BfWTdkY0FhVD5PbW5QYCUgUWdwKT9ZYE1yPmY+KXpaaVlZKGZzL00wQ2ErXSY+JEdpLnFlbyk9eS16Oi1KMT1kSjM5LzFqfD1ELV14QkhLQ3pCe251YSkjLWF6Rkk7VUhTdjh1UlJad05hbzxmMis0Vnd8a2xvKi0/QEcvKVIhMitQekMgfmx4KXxaKndYTFUvY1RGVWBrIDRCUzc+cD9MXS1dSSwwISt3KG5lKFdESC1hczJmbTVMfi9hdC9aPDtxS31+Z2ZkeWF0UnteR0ZvRExOQ2pyOlFuVSU/PyNffi5tSEIxQmxUaFhNUCZpdDJ1VmNeKzRzJl9XKCA9JWMjNyBfWFNlZ3NZfG9CdVRJNjljbW89UilNIUBeaHtvVmtmeXZdY3QpVEU3YilIPVsjfmF6fEpsPmNEZTE+W1ZAViR1U2hbYjdpa2wwQCxrQ19dVWl1U2hLcF57W155dm03XlRUVmEqQmJ9UURkUkV9PnB4K0ghaVB1bzJwK0R+dkQmcyh9WDY2ciVGZXhrYDBtbmNgXUdRc3x7M3U/VTdqUWxFaDgyQDJzeUtofXp9VTguPG8gZUI3al4sbjRtYExZSCk5UnY8YkM6eV57fSVfSl5YLU88JHVISSpxOV9wKWI9Sit9SHZyKiFfTXR2Vl9KaXp6RDNATF1UWShVX3F6ZlBgaDw1RG4lIzgzLGp9WXcudislfDhgeUs4LyptXzs1fVlvPkMuISBNQW0tSlBPPjxXNl8vVGNMSmc3dVlrZkI7VGZTXjwhaHlUJWVyPTxgL0cmNWdGZmRgJiBVPm8me35LVm9vdTQ9eGdJe0BnYFkvQDlsfm00IDQxOH5kMFlXUHg9NV0lREh0IVREZCAqI1koeWRaYnJ4Mio/KXFWbiMmSnxXQkMlY3ckVUV4O0c/dlI6a0pUXmozfDgzKGA/PUBuRT9zTHMqXWdgPTxHXU87c3BSanM6VWhRLz8kZEhGXS9oZEhMRVBFVjZocF4=",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
    }

    response = requests.post(url, headers=headers, data=payload)
    res = response.json()
    return res['access_token']





import random
import time
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from seleniumwire import webdriver as webdriver
import gzip

def get_airbound_cookiess():
    
    all_cookie=[]
    
    # Set up Chrome options
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-breakpad")
    options.add_argument("--disable-component-update")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-domain-reliability")
    options.add_argument("--disable-features=TranslateUI,BlinkGenPropertyTrees")
    options.add_argument("--disable-hang-monitor")
    options.add_argument("--disable-ipc-flooding-protection")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-prompt-on-repost")
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--disable-sync")
    options.add_argument("--force-color-profile=srgb")
    options.add_argument("--metrics-recording-only")
    options.add_argument("--safebrowsing-disable-auto-update")
    options.add_argument("--enable-automation")
    options.add_argument("--password-store=basic")
    options.add_argument("--use-mock-keychain")
#     options.add_argument("--headless")
    options.add_argument("--user-data-dir=/tmp/user-data")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--v")

    # Set up Chrome service
    service = Service(r"C:\Users\Adil Anwar\Downloads\chromedriver.exe")  # Provide the path to your chromedriver executable
    service.start()

    # Launch the browser
    driver = webdriver.Chrome(service=service, options=options)
#     driver = wiredriver.Chrome(service=service, options=options)

    # Set a random user agent
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ]
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": random.choice(user_agents)})

    # Visit Google
    driver.get('https://www.google.com')

    
    # Find the search bar and type the URL
    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.send_keys('https://www.swiss.com/lhg/gb/en/o-d/cy-cy/london-gb-frankfurt', Keys.RETURN)
    

    # Wait for the page to fully load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="search"]//a'))
    )

    # Find the first search result link
    first_result_link = driver.find_element(By.XPATH, '//div[@id="search"]//a')

    # Click on the first search result link
    first_result_link.click()

    # Wait for the page to load
    time.sleep(3)
    
    try:
    
        # Wait for the button to appear
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-link[aria-label='Close']")))

        # Click the button
        button.click()

        time.sleep(1)
    except:
        pass
    
    
     # Handle cookies pop-up if present
    try:
        accept_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cm-acceptAll"]'))
        )
        accept_button.click()
    except:
        pass
    
    time.sleep(2)
    
    
    # Scroll down the page by 500 pixels
    driver.execute_script("window.scrollBy(0, 500)")
    
    time.sleep(1)
    
    driver.execute_script("window.scrollBy(0, 500)")

    # Introduce a delay of 0.5 seconds
    time.sleep(1)

    # Scroll up the page by 500 pixels
    driver.execute_script("window.scrollBy(0, -500)")
    time.sleep(1)
    
    driver.execute_script("window.scrollBy(0, -500)")
    time.sleep(2)
    

    time.sleep(4)


  

    # Introduce a random delay
    time.sleep(random.uniform(1, 3))

    # Scroll to the calendar button
    calendar_button = driver.find_element(By.CLASS_NAME, 'form-group.calendar-input')
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", calendar_button)

    # Introduce a random delay
    time.sleep(random.uniform(1, 3))

    # Click the calendar button
    calendar_button.click()

    # Introduce a random delay
    time.sleep(random.uniform(1, 3))

    # Wait for the first button to be clickable    # THIS CAN BE IMPROVED
    oneway_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'checkbox-like'))
    )

    # Click the first button
    oneway_button.click()

    # Introduce a random delay
    time.sleep(random.uniform(1, 3))

    # Wait for the button to be clickable   # THIS CAN BE IMPROVED
    date_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//td[@tabindex="-1" and @data-date="2024-04-27"]'))
    )

    # Click the button
    date_button.click()

    # Introduce a random delay
    time.sleep(random.uniform(1, 3))

    # Wait for the continue button to be clickable      # THIS CAN BE IMPROVED
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'calendar-footer-continue-button'))
    )

    # Click the continue button
    continue_button.click()

    # Introduce a random delay
    time.sleep(random.uniform(1, 3))

    # Wait for the flight button to be clickable      # THIS CAN BE IMPROVED
    flight_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'searchFlights'))
    )

    # Click the flight button
    flight_button.click()

    # Introduce a random delay
    time.sleep(random.uniform(20, 30))   # THIS CAN BE IMPROVED
    
        # Wait for the page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

    # Find the scroll button element
    scroll_button = driver.find_element(By.CLASS_NAME, 'upsell-back-button')

    # Function to scroll to the element in small random steps
    def scroll_to_element(element):
        target_offset = element.location_once_scrolled_into_view['y']
        current_offset = driver.execute_script('return window.scrollY;')
        distance = abs(target_offset - current_offset)

        # Determine step size based on distance
        step = min(200, distance)  # Adjust 200 as needed

        # Scroll in one go if distance is small
        if distance < 200:
            driver.execute_script(f'window.scrollBy(0, {target_offset - current_offset});')
            return

        # Scroll in small random steps
        while distance > 0:
            direction = 1 if target_offset > current_offset else -1
            step = min(step, distance)
            driver.execute_script(f'window.scrollBy(0, {direction * step});')
            distance -= step
            time.sleep(random.uniform(0.1, 0.5))  # Random sleep between steps

    # Scroll to the element using small random steps
    scroll_to_element(scroll_button)

    # Introduce a random delay
#     time.sleep(random.uniform(1, 3))

    
#     # Find both "Next" and "Previous" buttons
#     next_button = driver.find_element(By.CLASS_NAME, 'more-dates-future-btn')
#     previous_button = driver.find_element(By.CLASS_NAME, 'more-dates-past-btn')

#     # Randomly select either the "Next" or "Previous" button and click it
#     random_button = random.choice([next_button, previous_button])
#     random_button.click()

#     time.sleep(random.uniform(9, 20))



    # Filter requests for the specific URL
    target_url = "https://api-shop.swiss.com//v1/one-booking/search/air-bounds"
    target_requests = [request for request in driver.requests if target_url in request.url]

    cooks = []
    # Print details and status codes for each request
    for request in target_requests:
        print("Request URL:", request.url)
        print("Request Method:", request.method)
        print("Request Headers:")
        for header, value in request.headers.items():
            print(f"{header}: {value}")
        if request.response:
            print("Response Status Code:", request.response.status_code)
            print("Response Body:", request.response.body)
            decompressed_body = gzip.decompress(request.response.body).decode('utf-8')
            cooks.append(decompressed_body)
        else:
            print("No response received for this request.")
        print()
        
    all_cooks = []
    cookies = driver.get_cookies()
    all_cooks.append(cookies)




    # Get cookies
#     cookies = driver.get_cookies()

    # Close the browser
    driver.quit()
#     all_cookie
#     main_cookie=[i[1] for i in all_cookie[0] if i[1].startswith('_abck')][0].split(' ')[0]
#     return main_cookie,cooks
    return cooks,all_cooks
    



cookke,all_cooks=get_airbound_cookiess()

cookie_main=[i['value'] for i in all_cooks[0] if i['name']=='_abck'][0]

import requests
import json
def get_airbound_cookie(cookie_main):
    url = "https://api-shop.swiss.com/v1/one-booking/search/air-bounds"


    payload = json.dumps(    
    {
      "commercialFareFamilies": ["DEMALLFPP"],
      "itineraries": [
        {
          "departureDateTime": "2024-06-26T00:00:00.000",
          "originLocationCode": "LON",
          "destinationLocationCode": "FRA",
    #         "flexibility": "3",
          "isRequestedBound": True
        }
      ],
      "searchPreferences": {
        "showSoldOut": False,
        "showMilesPrice": False
      },
      "travelers": [
        {
          "passengerTypeCode": "ADT"
        }
      ]
    }
    )




    payload_round = json.dumps(
    {
      "commercialFareFamilies": ["DEMALLFPP"],
      "itineraries": [
        {
          "departureDateTime": "2024-06-12T00:00:00.000",
          "originLocationCode": "LON",
          "destinationLocationCode": "DXB",
          "isRequestedBound": True
        },
        {
          "departureDateTime": "2024-06-30T00:00:00.000",
          "originLocationCode": "DXB",
          "destinationLocationCode": "LON",
          "isRequestedBound": False
        }
      ],
      "searchPreferences": {
        "showMilesPrice": False
      },
      "travelers": [
        {
          "passengerTypeCode": "ADT"
        }
      ]
    }

    )






    headers = {'Ama-Client-Ref':'51738419-f015-4d66-b254-50e3b30f0a02:x',
        'Content-Length':'274',
    'Content-Type': 'application/json',
      'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
      'callid': '51738419-f015-4d66-b254-50e3b30f0a02:x',
      'sec-ch-ua-mobile': '?0',
      'authorization': f'Bearer {get_token()}',
    #   'akamai-bm-telemetry': 'a=3635805540034FFCDE6C800F12C8C166&&&e=MEE0MTFEOEM0RDcyMTlFMTNCNUI1QjE5N0E4OEE3ODR+WUFBUVJRVmFhTHJURTAyUEFRQUF6bUR3WEJjempRUXJhay9KVDVKa2ZwYjhjWEdIR1BTQ2ZiRnlLbVhVRE8xN1dORUpsYjhBbVFkWUVIdnU0SVdRNUdOWU54S3c5TGJ3NEJ1WW4wWEdzS2U0N21IU3RmVndPc3R2Vkl0R3pXcktDTUV1T1VESGdVZVVaRUJYK0lOM3BzN2kzS3VxZWtXVHVsUE5VRWwxUG5QSmg0UjEwQUdWbDRjUHJjQnVxNERYbWEvUCsrMDNPVkl4NlFBQVZFS0JJSmpHTktrVkthUXZiMHJuZEpVN2FWd1JHZk1aL3VBVjhqejJTa2cvY2hXRlpLcXE1WWpwTitpT2FzZWtONG5JS29qbFpNQ2FzVVAxeXFCM1BmTExvejJIU0V4UVlVa0RCMGNxa1JhV29RMW5RajFWSWpzTnhCMjJMSVBQdjhkL2pzdmFPQzhPRVI0dUdqZDB5TTRmeFBxeUNoWG0zOG1GUVBmRFg0UnRGeDZxRzQ2aXJtMER0dzNKdThZZHVLRXhzUlhiTHBvMjdGUExOa2FLVlBnbnRmYnNmMGg5TWd6TGsvNkFvSm9rU1hUYVdEcWZpUUU0TXhOMDNDemh1V0dQUkE4eDRnTExsM09kL1ZML3F3L3h5R05TZGY2Uy93Q2dUZXQxVmJQMkpkRm8zd1lzTVh5eThlSThJckd1ZnplRGZiN0V4ODMwTXc9PX40NDY5MDU5fjQ0MDQwMTc=&&&sensor_data=Mjs0NDY5MDU5OzQ0MDQwMTc7NiwyNiwwLDAsMiw1NTtyLSAqaDUsRUpzZilbXkVIM2BuQT5fPV55ZiR0cC9+SHYqMDJdKmhxXSU6b1pEZzd+a15NZlQzVGthfUAvZC8zRDApbVM4bGguMm1ve1MvaXZTWDptL2kpUng6TFUpV0NDZmQkcyZ3dk5yeSBZfGA9JU1GJnE5NGAqZEZddGdicDkkaV90LXtpSX0mL3A3L292bHNEOFpJfFRoJThxdFo/I0ZdcFtPPEVzJS87cUlTcn55fFRMQkBzSW1PM3htOjIuci8/NEJFQi9oKD56XVFLY2JpaChtdUkyUGY/MT1DbWw8ZDFGYzpxI1RHUW1HfDUkYiooRDxAKGotRzYkNj5bfU55SW0vQkhWd2FrOFdMPUxAPDhNTmpGO2chbkdaWmJzVVRyfT9XcGNSaUgyJi0uYmo1PWNjQlh9eUg6M1NzQmdGbktBOSt7dXlEeGJ3Yzc8WSNEXWAge3pBMV0sI3N6STo6SSVURDNiNzMuPlogS3w5by9kPyl2flYgNFUgfH5TdlBjMk85MzU1RE1MdzkkWG9yaU0sQ3NTWTJBOz4xS3A9eDc4Q1J+LT9yUVRVJkVvMz8tMTVha2VAMjdGdj0jQShBOiFzMmclLmxRYl4wVS9vVSNfeENLXjlxTER+WkkxfGhmOT1eaGF1cGRsKGIhX019O2g5IClPJm9pcVk1azhuIUJaJjhQQXpNZFRPY1UpTUVJfDxmdVtJUjNlZ1RmPG5SakksWSYzfSBGPHpwJXh8QE9xenUma3lYXiNqMjY1QVlkTVszbDx4ekIjOnJYY0hbWjF+Zz4wbFNZI09AdGMpQT0zcHd3Oy8lVWA/VDlUblZAZ3FjQVBFfiNDUVMzT3BGQUFvPWtiJjY5TGpnNVJtN0p6K1ldaXopNSo1N1trWFdgfWVXPzYvPCYgdWJ8NntEWHdJRlFkWC8kUT5xSyM6Py02XWsrKFt6N2BQNTM6LUZIIXwranMrPDtge05CSl8oVmNjM3pONT0qc1pPM3xtbVdeSi5bJilFeGkyclMuLD5LeUEtaVVCWVBkNWNsJjB3S21XKE43bWlfbXMyQ19VPzQhPWJOO1QtUyRCJFF8SUFxPiBFdFFUYCY2TV9qSSV4Ky51V1FWL3U+Uy1baltVXjkpKzY2blVYVUgmMkFbVCZlPVtDNEkrejUkVD1FT1NSZy5PKnk5SilRZU5fbC9QcmpEI0wveE0lJDt0anVeejRaLzNbVVFXQzZBMkMkUj97YUIoOmpgPCN7Q0E9Mk9yVTo7Pk85ezlaWz9yMndYZD5tLVNuUFldRG88aV9UanZGYCQyXSgwYEJUQVhrT30sZmo6KE8oNzlNTCxxTHVDbFQpWnxJU19IOEUqVWdIa2Agc1NIdFVkdGJZVWpCY0NzZTp8QmYmOi1dVlJ9QkA0Mm4haVQsP31gLiNDVn5LPW1YN31QIDlWQWpvblA3KyZ4d3lJKEEhRWVbVyAqOlsuVSxJflRYMiVaTXE6JClPcGVlcmBsQzlZXjdwN1Q3RSQ/QSFqUixOenhran5XLTswTERXT11FNWQqYk5ZbVtAP2wgX2ItfkMtVTdFSkUoY1Vzei8oQDkpUjAuPWcraS8jJlU1OjtSSGIuVWN8cXIpc0BIXl46WSVDUz4uWms8aW1jcmdvSUx9TFpqQmlULzMrWWN9NVBJQyNfcHsjdT5xdm8gJDR5MDZDL0YuamJiIzxobEJIdW90SXJsZER2I3N7czI4SzUoSndudEFuW1FTUGN1aFBDK0F5byQ4LV1nWjhhTjloL24hdS5QMiY1Rl17SiRIZVEjby9MNyNJNTs9W3ArME9PUkcoUHVkIy9xOV9CYzQ9UD1KRUVlMXdna0xdSm10REdZPWN6IH1FVElrXWFgfkcyMU9mMjQ2NylCOWskQWcoNUg2MWMuRXRfXj5eUnRjWyomPEU/dkJEPUd7fWB7XlIxMCsjTSstJVR4TCpmRTNlQGQ1Mm1Rb089YWt0JkhVMkdZJFJefVJCWHA9WSZZUDVuQVpsel8tRkRueFhzZXtgdjosQXtgenJOI2o/MyN1QTZZN0pdM1UoMU5tVSZmKzV2eGJnJlFZVThlVTBpQiVaViNlYnduUWNxQ2ROc2Y/bjltbzB5bSE2TSlJLS1EOWVTU1o+Nip5PU97RzdqXTh2UXMsS3BoMGs/dVNFUDlZcCxiU3JIRE84TjdbPD9AdHM1dzZVQzhRQzh9diYqPVVMUCB6QVhkW3cue1k9enpgVSVsTj9jRWwxe3Jsd3whMSk5b1ssbVRSM0AqbV9HRjs2aXFkZDt3M0YubSwpRktiYGRSTFltVkswWkd2UiV4WF82K159LDd0PjZPLVFZWCBIfkskZC5JRi1NOSYveCZCaCBRSFIkdXR9R3dEPWdyXTFyTHh1K3ssaT4tSHJENEdudVYmbXdINHNxZilfQ1d8O1dPbndlRWdKfnt4aERlaU48NmQ9cSVZM2M3Xmg4OiQrPVVwbV8hNXZWZj9WJEFHVlk8Wnt9OilwKylLTiU2REx0Ry06Z1I4XXkpJkBLZ3U3MjlAWUxPTitEWyhrc2Z4RWooQntKeTI1IEhXezBDe2w6LldMcUM8WltvM004WFZgO0hlYnN+T0JZOkl0JlRoMVY+TiprNCt6RWxCe1c9LFI2U3RtbkBvW1dOR05fSVUwKHEzW3hOTUpqNXR1S2FRcyxwbUlRKmhhUXEtXyBTdE1RfSMoTGxhR2dSXl49dW1LI3g8JiAuMF5BciV8Vy1pcHNfKGEpeE5VLVRdRz96cFA8ZTtMVUB5KTRieFp9YDVwI1Zobko2Q10yaEUmVGAwSWtidFh7aD1fZ294QmJULm46ZEVJbFlESGMwXzIkW2pKP31ddiR6bCE1Wy57UjtsZTNpbyN5cTFKLmRoTEx5ajw3fVFyQismOChOW0chKF05UXF1KEVlXlchQSRyIHkzcX5hWV4+NyNRbEBzeVJXLXt0JXFyb2o+ZVA3elVTPV1OVTwwaHhgbHl9US8seH0=',
      'content-type': 'application/json',
      'accept': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
      'cache-control': 'max-age=0',
    #   'ama-client-facts': 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiJmYWN0IiwiY2FiaW4iOiJFQ09OT01ZIn0.',
      'ama-client-ref': '51738419-f015-4d66-b254-50e3b30f0a02:h',
      'sec-ch-ua-platform': '"Windows"',
      'Sec-Fetch-Site': 'same-site',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Dest': 'empty',
      'host': 'api-shop.swiss.com',
      'Cookie': f'_abck={cookie_main};'
    }

    response = requests.request("POST", url, headers=headers, data=payload_round)# data=payload)

    print(response.text)
    
    return response.text



get_airbound_cookie(cookie_main)
