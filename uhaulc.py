from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from time import sleep
from datetime import datetime

# Specify the location of the ChromeDriver
chrome_driver_path = 'C:/Users/student/OneDrive/Desktop/WebScraper/chromedriver.exe'
chrome_binary_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

# Create Chrome options and set the binary location
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path

# Create a new instance of the Chrome driver with Chrome options
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Read the input file (CSV file in the same directory)
input_file = 'input.csv'
input_data = pd.read_csv(input_file)
extracted_data = []

# Iterate through the rows in the input data
for index, row in input_data.iterrows():
    pickup_location_input = row['Pick Up Location']
    dropoff_location_input = row['Drop Off Location']

    # Open the webpage
    driver.get('https://www.uhaul.com/Truck-Rentals/')
    sleep(3)

    # Find the pickup location input field using its XPath
    pickup_location = driver.find_element(by='xpath', value='/html/body/main/div/div/div/div[1]/div[1]/form/fieldset/div/div[2]/div[1]/label/input')
    # Clear any existing value in the pickup location input field
    pickup_location.clear()
    # Take input for Pick up
    pickup_location.send_keys(pickup_location_input)

    # Find the drop-off location input field using its XPath
    dropoff_location = driver.find_element(by='xpath', value='/html/body/main/div/div/div/div[1]/div[1]/form/fieldset/div/div[2]/div[2]/label/input')
    dropoff_location.clear()
    # Take input DROP OFF
    dropoff_location.send_keys(dropoff_location_input)

    # Get the current date and format it as 'MM/DD/YYYY'
    current_date = datetime.now().strftime('%m/%d/%Y')

    # Find the date input field using its XPath
    date_input = driver.find_element(by='xpath', value='/html/body/main/div/div/div/div[1]/div[1]/form/fieldset/div/div[2]/div[3]/label/input')

    # Clear any existing date in the field
    date_input.clear()

    # Type the current date into the field
    date_input.send_keys(current_date)

    # Find the "Get Rates" button using its XPath
    get_rates_button = driver.find_element(by='xpath', value='/html/body/main/div/div/div/div[1]/div[1]/form/fieldset/div/div[2]/div[4]/button')

    # Click the "Get Rates" button
    get_rates_button.click()


    # Give the page time to load
    sleep(3)

    # Extract the pickup and dropoff locations
    locations_xpath = "//h1"
    locations_element = driver.find_element_by_xpath(locations_xpath)
    locations_text = locations_element.text.strip()
    pickup_location, dropoff_location = locations_text.split(" to ")
    pickup_location = pickup_location.split("for ")[1] if "for " in pickup_location else pickup_location
    dropoff_location = dropoff_location.split(" on ")[0] if " on " in dropoff_location else dropoff_location

    # Locate and extract the truck types
    truck_type_xpath = "//h3[@class='text-2x']"
    truck_types_elements = driver.find_elements_by_xpath(truck_type_xpath)
    truck_types = [element.text.strip() for element in truck_types_elements]

    # Locate and extract the rates
    rate_xpath = "//b[@class='block text-3x medium-text-2x text-callout medium-text-base']"
    rate_elements = driver.find_elements_by_xpath(rate_xpath)
    rates = [element.text.strip() for element in rate_elements]

    # Locate and extract the moving types
    moving_type_xpath = "//dd[@class='text-bold text-xl']"
    moving_type_elements = driver.find_elements_by_xpath(moving_type_xpath)
    moving_types = [element.text.strip() for element in moving_type_elements]

    # Build the DataFrame
    for truck_type, rate, moving_type in zip(truck_types, rates, moving_types):
        extracted_data.append({
            "Pickup Location": pickup_location,
            "Dropoff Location": dropoff_location,
            "Rate": rate,
            "Truck Type": truck_type,
            "Moving Type": moving_type
        })

df = pd.DataFrame(extracted_data)

# Save to Excel
current_datetime = datetime.now().strftime("%B-%d-%Y--%H-%M-%S")
filename = f"{current_datetime}-output.xlsx"
df.to_excel(filename, index=False)

# Close the driver
driver.quit()
