import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from requests.api import request

url = "https://myanimelist.net/topanime.php?limit=0"
headers = {"Accept-Language": "en"}

results = requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

# Storage
ranks = []
titles = []
score = []

# Start of information gather
anime_div = soup.find_all('tr', class_='ranking-list')

for container in anime_div:

    # Gets the ranking of each anime
    ranking = container.span.text
    ranks.append(ranking)

    # Gets the Title
    name = container.h3.a.text
    titles.append(name)

    # Gets the score
    points = container.find('span', class_='text on score-label score-9').text if container.find('span', class_='text on score-label score-9') else container.find('span', class_='text on score-label score-8').text
    score.append(points)

# Data Frame
animes = pd.DataFrame({
    'Rank': ranks,
    'Title': titles,
    'Score': score,
})

print(animes)
input("Press Enter to Exit")

animes.to_csv('Top 50 Animes.csv')