import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from requests.api import head

# The website i chose is Kabum, i also narrowed it down to only Video Cards, The "url" variable gets assigned the URL of the website
url = "https://www.kabum.com.br/hardware/placa-de-video-vga"

# Requests.get takes the contents of the website stored in the previous Variable, and gets saved in the "results" Variable
results = requests.get(url)

# From what i understood, this variable saves the information gathered from BeautifulSoup in a Format that lets Python read the Components of the page
soup = BeautifulSoup(results.text, "html.parser")

# This is the Storage of the information i want the bot to take.

brand = []
product = []
price = []
memory = []
ddr = []
availability = []

# After looking at the product page using the "Inspect" command, i've noticed that every product is from the div class "sc-fzqARJ eITELq", so i set the soup.find_all to get
# all the divs with that specific class, which then gets saved into products_div
products_div = soup.find_all('div', class_='sc-fzqARJ eITELq')
