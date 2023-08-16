
# U-Haul WebScraper

## Description
This script automates the process of web scraping using the Selenium library in Python. It uses the Chrome browser to fetch data from a webpage based on inputs provided in a CSV file.

## Dependencies
- Python
- Selenium
- pandas

## Setup Instructions
1. Ensure you have Python installed.
2. Install the required libraries using pip:
   ```
   pip install selenium pandas
   ```
3. Download the appropriate [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for your version of Chrome and place it in the specified path in the script.
4. Ensure you have Chrome installed and specify its path in the script.

## Usage Instructions
1. Prepare an 'input.csv' file with the required input data.
2. Run the script:
   ```
   python uhaulc.py
   ```
3. The script will read the input, visit the webpage, and perform the scraping tasks.

## Notes
- Make sure to adjust the paths for `chrome_driver_path` and `chrome_binary_path` according to your system setup.
- The script assumes a specific structure for the input CSV file with columns 'Pick Up Location' and 'Drop Off Location'.
- Ensure that the Chrome browser is not being used for other tasks while the script is running to avoid interruptions.
