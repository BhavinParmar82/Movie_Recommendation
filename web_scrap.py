# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:04:55 2023

@author: Bhavin
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

# define the website to scrape and path where the chromediver is located
website = 'https://www.movieposters.com/'
service = Service('C:/Users/bhavi/Downloads/chromedriver') # write your path here
   
#movie_list = ["Speed", "Ghost Rider", "Stuart Little"]   
    
def get_poster(movie_list):
    movie_list = [i.replace("'", "") for i in movie_list if i.find("'")]
    poster_list = []
    for movie in movie_list:
        # define 'driver' variable
        driver = webdriver.Chrome(service=service)
        driver.get(website)    
        
        search = driver.find_element("id", "searchField")
        search.clear()
        search.send_keys(movie)
        search.submit()
        time.sleep(5)
        
        try:
            image_element = driver.find_element(by = 'xpath', value="//img[@alt=" + "'" + movie + "'" + "]")
            image_url = image_element.get_attribute("src")
            image_url = "<img src=" + image_url + ">"
        except NoSuchElementException:
            image_url = "Image Not Found"
            
        poster_list.append(image_url)
        driver.close()
    return poster_list

get_poster(['Speed'])

get_poster(['Our Kind of Traitor', 'Civil Brand', 'Phone Booth', 'Margin Call', 'Zipper'])
