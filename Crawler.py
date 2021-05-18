import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from requests.api import head

# The website i chose is Kabum, i also narrowed it down to only Video Cards.
url = "https://www.kabum.com.br/hardware/placa-de-video-vga"

results = requests.get(url)

soup = BeautifulSoup(results.text, "html.parser")

# Storage
brand = []
product = []
price = []
memory = []
ddr = []
availability = []

# After looking at the product page using the "Inspect" command, i've noticed that every product is from the div class "sc-fzqARJ eITELq", so i set the soup.find_all to get
# all the divs with that specific class, which then gets saved into products_div
products_div = soup.find_all('div', class_='sc-fzqARJ eITELq')
