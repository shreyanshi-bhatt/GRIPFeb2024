from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Edge()  # You can change the webdriver based on your browser choice
driver.maximize_window()  # instructs the Selenium WebDriver to maximize the browser window to ensure consistent
# behavior across different screen sizes.

# Define the website URL
url = "https://www.thesparksfoundationsingapore.org/"


# Function to check if an element is present
def is_element_present(how, what):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((how, what)))
        return True
    except:
        return False


# Function to test each page
def test_page(page_url, elements):
    driver.get(page_url)
    print("\nTesting", page_url)
    for element in elements:
        if is_element_present(*element):
            print(f"{element[1]}: Passed")
        else:
            print(f"{element[1]}: Failed")


# List of pages and elements to test
pages_to_test = [
    ("", [
        (By.CLASS_NAME, "logo"),
        (By.CLASS_NAME, "navbar"),
        # Add more elements from the home page
    ]),
    ("about/vision-mission-and-values/", [
        (By.XPATH, "//h4[contains(text(),'About Us') or contains(text(),'About')]"),
        (By.XPATH, "//a[contains(text(),'Vision, Mission and Values')]"),
        # Add more elements from the About Us page
    ]),
    ("contact-us/", [
        (By.XPATH, "//h4[contains(text(),'Address')]"),
        (By.CLASS_NAME, "contact")
    ]),
    ("links/ai-in-education/", [
        (By.XPATH, "//a[contains(@href,'https://www.forbes.com/sites/sebastienturbot/2017/08/22/artificial"
                   "-intelligence-virtual-reality-education/')]"),
        (By.CLASS_NAME, "copyright")
    ]),
    ("programs/workshops/", [
        (By.CLASS_NAME, "footer"),
        (By.XPATH, "//div[contains(@class,'blog')]")
    ])
    # Add more pages and elements to test
]

# Iterate over each page and test the elements
for page in pages_to_test:
    test_page(url+page[0], page[1])

# Close the WebDriver
driver.quit()
