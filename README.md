# Steam Web Scraper

## Overview

This Python script allows you to scrape data from the Steam Store website, including information about top-selling games such as their titles, release dates, prices, discounts, and discounted prices. It utilizes web scraping techniques using the BeautifulSoup library and data manipulation with pandas.

## Features

- Scrapes data from the Steam Store website for top-selling games.
- Retrieves game titles, release dates, prices, discounts, and discounted prices.
- Outputs the scraped data to an Excel file for further analysis.

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup library
- Pandas library

## Usage

1. Clone the repository to your local machine.
2. Install the required Python libraries:
```
pip install requests beautifulsoup4 pandas
```
4. Run the script:
```
python SteamScrape.py
```
6. The script will scrape the data and save it to a file named `steam.xlsx`.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project is inspired by the need to gather data from the Steam Store website for analysis and research purposes.
- Special thanks to the developers of the BeautifulSoup and pandas libraries for providing powerful tools for web scraping and data manipulation.
