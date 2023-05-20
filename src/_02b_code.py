from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

# define the website to scrape and path where the chromediver is located
website = 'https://www.imdb.com/'
service = Service('C:/Users/bhavi/Downloads/chromedriver') # write your path here
      
def get_poster(movie_list):
    poster_list = []
    for movie in movie_list:
        # define 'driver' variable
        driver = webdriver.Chrome(service=service)
        driver.get(website)    
        search = driver.find_element("id", "suggestion-search")
        search.clear()
        
        movie = movie.title()
        search.send_keys(movie)
        time.sleep(5)
        search.submit()
        time.sleep(5)
        
        try:
            driver.find_element(by = 'xpath', value='//a[@class="ipc-metadata-list-summary-item__t"]').click()
            image_element = driver.find_element(by='xpath', value='//img[@class="ipc-image"]')
            image_url = image_element.get_attribute('src')
        except NoSuchElementException:
            image_url = "Image Not Found"
            
        poster_list.append(image_url)
        driver.close()
    return poster_list
   