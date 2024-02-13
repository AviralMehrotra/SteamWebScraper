import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time

url = "https://store.steampowered.com/search/results/?query&start=1&count=50&dynamic_data=&sort_by=_ASC&supportedlang=english&snr=1_7_7_7000_7&filter=topsellers&infinite=1"


def totalResults(url):
    response = requests.get(url)
    data = dict(response.json())
    totalResults = data['total_count']
    return int(totalResults)


def getData(url):
    response = requests.get(url)
    data = dict(response.json())
    return data['results_html']


def parseData(data):
    gameList = []
    soup = BeautifulSoup(data, 'html.parser')
    games = soup.find_all('a', class_='search_result_row ds_collapse_flag')
    for game in games:
        title = game.find('span', class_='title').text

        releaseDate = game.find('div', class_='search_released')
        releaseDate = releaseDate.text.strip() if releaseDate else "Not Available"

        price = game.find('div', class_='discount_original_price')
        price = price.text.strip() if price else None
        discount = game.find('div', class_='discount_pct')
        discount = discount.text.strip() if discount else "0%"

        discountedPrice = game.find(
            'div', class_='discount_final_price')
        discountedPrice = discountedPrice.text.strip(
        ) if discountedPrice else "Not Available"

        if price:
            games_elements = {
                'Title': title,
                'Release Date': releaseDate,
                'Price': price,
                'Discount': discount,
                'Discounted Price': discountedPrice
            }
        else:
            games_elements = {
                'Title': title,
                'Release Date': releaseDate,
                'Price': discountedPrice,
            }
        gameList.append(games_elements)
    return gameList


def outputData(gameList):
    gameData = pd.concat([pd.DataFrame(i) for i in gameList])
    gameData.to_excel('steam.xlsx', index=False)
    print("Data has been written to steam.xlsx")
    print(gameData.head())
    return


# data = getData(url)
# gamesList = parseData(data)
# outputData(gamesList)
# # print(gamesList)

results = []
for x in range(0, totalResults(url), 50):
    data = getData(f"https://store.steampowered.com/search/results/?query&start={
                   x}&count=50&dynamic_data=&sort_by=_ASC&supportedlang=english&snr=1_7_7_7000_7&filter=topsellers&infinite=1")
    gamesList = parseData(data)
    results.append(gamesList)
    print(f"Scraping {x} of {totalResults(url)}")
    time.sleep(10)

outputData(results)
