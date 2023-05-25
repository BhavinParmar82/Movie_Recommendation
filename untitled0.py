# -*- coding: utf-8 -*-
"""
Created on Sun May 21 08:44:28 2023

@author: Bhavin
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

# define the website to scrape and path where the chromediver is located
website = 'https://www.imdb.com/'
# write your path here
service = Service('C:/Users/bhavi/Downloads/chromedriver')

driver = webdriver.Chrome(service=service)
driver.get(website)
search = driver.find_element("id", "suggestion-search")
search.clear()

movie = "Bubble Boy"
movie = movie.title()
search.send_keys(movie)
time.sleep(5)
search.submit()
time.sleep(5)

driver.find_element(by='xpath', value='//a[@class="ipc-metadata-list-summary-item__t"]').click()
image_element = driver.find_element(by='xpath', value='//img[@class="ipc-image"]')
image_url = image_element.get_attribute('src')
# print(image_url)

text_element = driver.find_element(
    by='xpath', value='//p[@data-testid="plot"]')
# text_element.text
print(text_element.text)

credit_element = driver.find_element(by='xpath', value="//ul[@class='ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt']")
credit_element1 = credit_element.find_elements(by='xpath', value='//li[@data-testid="title-pc-principal-credit"]')

import pandas as pd    
import re
data = []
for li in credit_element1:
    data.append(li.text)
    
    
converted_data = []
for item in data:
    parts = re.split(r'(?<=[a-z])(?=[A-Z])', item)
    converted_parts = []
    for part in parts:
        if re.search(r'[a-zA-Z]', part):
            converted_parts.append(part)
    converted_data.append(', '.join(converted_parts))
    
    
# Split the data on the newline character and create a dictionary
data_dict = {}
for item in converted_data:
    key, value = item.split('\n')
    data_dict[key] = value

# Create a DataFrame from the dictionary
df = pd.DataFrame.from_dict(data_dict, orient='index', columns=['Data'])

# Print the DataFrame
print(df)
