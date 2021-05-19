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

# Storage, this is just a template to how i think i'll separate the information, may change.
brand = []
product = []
price = []
memory = []
ddr = []
availability = []

# After looking at the product page using the "Inspect" command, i've noticed that every product is from the div class "sc-fzqARJ eITELq", so i set the soup.find_all to get
# all the divs with that specific class, which then gets saved into products_div,
# the problem now is that, this returns nothing, so i'm either choosing the wrong tag to get the information, or i am not getting the information in the first place.
# testing now to see which one it is.
products_div = soup.find_all('div', class_='sc-fzqARJ eITELq')
