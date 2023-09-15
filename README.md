
# U-Haul WebScraper

## Introduction

The U-Haul WebScraper is a Python-based automation tool designed to fetch targeted pricing information directly from U-Haul's official website. Manually gathering this data can be both tedious and prone to errors. This script efficiently streamlines the data extraction process by leveraging Python's powerful libraries. Its primary focus is capturing details corresponding to the 'Pick Up Location' and 'Drop Off Location' for U-Haul truck rentals.

## Objective

The primary goal of this project is to gain insights into population shifts between US cities by analyzing U-Haul pricing. The cost structure of U-Haul is a reflection of the supply and demand dynamics of inter-city relocations. This project aims to gather U-Haul pricing data for various city routes specified in the `input.csv` file by leveraging a tailored script that harnesses web scraping techniques. Each entry in this file defines a pair of 'Pick Up Location' and 'Drop Off Location.'

The collected pricing data can also be instrumental in analyzing:
1. **Housing Demand**: High relocation rates, inferred from elevated U-Haul prices, can indicate increased housing demand in certain cities.
2. **Job Market Fluctuations**: A surge in the incoming population in certain cities might suggest job opportunities or booming industries.
3. **Seasonal Trends**: Analyzing the price data across different seasons can reveal peak times for inter-city moves.
4. **Predictive Analysis Potential**: Predictive models can forecast future pricing trends or shifts in demand between various city pairs.

## Dependencies

- **Python**: The backbone of this script.
- **Selenium**: Used to mimic human browsing behavior.
- **Pandas**: Essential for data management.

## Setup Instructions

1. Ensure that Python is up and running on your system.
2. Install the required libraries:
```
pip install selenium pandas
```
3. Obtain the EdgeDriver compatible with your Microsoft Edge version from the Microsoft Developer Site.
4. Store the EdgeDriver in a designated directory.
5. Validate the installation of EdgeDriver on your machine.
6. Update the path for your directory in the code:
   - Copy the file path.
   - Update it in the code `edge_driver_path = "<YOUR_PATH>"`.

## Usage Instructions

1. Create a CSV file titled `input.csv` with two primary columns:
   - 'Pick Up Location'
   - 'Drop Off Location'
   
Example for `input.csv`:

```
Pick Up Location, Drop-Off Location
New York City, NY, Los Angeles, CA
...
```

2. Run the script:
```
python Scraper.py
```

3. Upon execution, the script will:
   - Read and process entries from the `input.csv` file.
   - Launch a new Microsoft Edge browser session.
   - Access the specified Uhaul truck rental webpage.
   - Extract the data for all city pairs.
   - Append the output into the `uhauloutput` file.

### View Results

Open `uhauloutput.xlsx`. 
**Note**: Ensure this file is closed while running the program.

## Limitations

- **Captchas**: The script may fail if a CAPTCHA challenge is triggered during scraping.
  - **Solution**: Using a VPN can sometimes bypass CAPTCHAs.
  
- **CSV Structure Dependency**: The script relies on the structure of `input.csv`. Any structure alterations need script modifications.
- Avoid using the Microsoft Edge browser manually during the scraping process.

## Things to Note

1. Personalize `edge_driver_path` based on your system’s configuration.
2. Ensure all files are saved in the same directory.
3. The note file controls the program's start point. To start from a specific inquiry, such as line 100 in the input file, place "100" in the note file. To start over, delete the note file or set the number to 0.

## Conclusion

The Uhaul web scraper script showcases the potential of automated data extraction for tasks involving repetitive website interactions. Tailored for Uhaul, this script's principles can be adapted for other web scraping tasks.
