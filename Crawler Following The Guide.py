import requests
from requests import get 
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# This is just so it filters the movies to get only English-Translated names.
headers = {"Accept-Language": "en-US, en;q=0.5"}

# The URL chosen here is the same as the guide i was following, it's the top 1000 movies in IMDB ranked by Popularity. 
url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

# Requests.get takes the contents of the website stored in the previous Variable, and gets saved in the "results" Variable.
results = requests.get(url, headers=headers)

# From what i understood, this variable saves the information gathered from BeautifulSoup in a Format that lets Python read the Components of the page.
soup = BeautifulSoup(results.text, "html.parser")

# This is the Storage of the information i want to scrape.
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

# After looking at the product page using the "Inspect" command, i've noticed that every product is from the div class "lister-item mode-advances", so i set the soup.find_all to get
# all the divs with that specific class, which then gets saved into movie_div
movie_div = soup.find_all('div', class_='lister-item mode-advanced')

# Creates a For loop, from what i understood this Cicles through every Div container
# that was stored in the previous variable for the information we want.
for container in movie_div:
 name = container.h3.a.text
 titles.append(name)

 year = container.h3.find('span', class_='lister-item-year').text
 years.append(year)

 runtime = container.find('span', class_='runtime').text if container.p.find('span', class_='runtime') else '-'
 time.append(runtime)

 imdb = float(container.strong.text)
 imdb_ratings.append(imdb)

 m_score = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
 metascores.append(m_score)

 nv = container.find_all('span', attrs={'name': 'nv'})

 vote = nv[0].text
 votes.append(vote)

 grosses = nv[1].text if len(nv) > 1 else '-'
 us_gross.append(grosses)

# This uses Pandas to create a DataFrame that organizes all the information adquired into a Table-like screen
# for ease of vewing.
movies = pd.DataFrame({
    'movie': titles,
    'year': years,
    'timeMin': time,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes,
    'us_grossMillions': us_gross,
})

# Data Cleaning (obviously i haven't mastered this, but i at least know a bit more about it, it's a process i didn't even know existed)
# the guide teached me to see the data types with .dtypes and to properly correct them.
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
movies['timeMin'] = movies['timeMin'].str.extract('(\d+)').astype(int)
movies['metascore'] = movies['metascore'].astype(int)
movies['votes'] = movies['votes'].str.replace(',','').astype(int)
movies['us_grossMillions'] = movies['us_grossMillions'].map(lambda x: x.lstrip('$').rstrip('M'))
movies['us_grossMillions'] = pd.to_numeric(movies['us_grossMillions'], errors='coerce')

# Converts the information saved into an Excel file.
movies.to_csv('movies.csv')

