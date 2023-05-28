from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import re
import pandas as pd

# define the website to scrape and path where the chromediver is located
website = 'https://www.imdb.com/'
service = Service('C:/Users/bhavi/Downloads/chromedriver') # write your path here
        
def get_moviedetails(movie_list):
    poster_list = []
    info = []
    plot = []
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(website)    

    for movie in movie_list:
        # define 'driver' variable
        search = driver.find_element(by="id", value="suggestion-search")
        #search = driver.find_element(by="xpath", value='//*[@id="suggestion-search"]')
        search.clear()
        
        movie = movie.title()
        search.send_keys(movie)
        time.sleep(5)
        search.submit()
        time.sleep(5)
        
        try:
            # To fetch movie poster
            driver.find_element(by = 'xpath', value='//a[@class="ipc-metadata-list-summary-item__t"]').click()
            image_element = driver.find_element(by='xpath', value='//img[@class="ipc-image"]')
            image_url = image_element.get_attribute('src')
            
            # To fetch movie plot
            text_element = driver.find_element(by='xpath', value='//p[@data-testid="plot"]')
            plot.append(text_element.text)
            
            # To fetch Director Name, Writer Name and Star Cast
            credit_element = driver.find_element(by='xpath', value="//ul[@class='ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt']")
            credit_element1 = credit_element.find_elements(by='xpath', value='//li[@data-testid="title-pc-principal-credit"]')

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
            converted_data = [item for item in converted_data if item.strip()]
                
            # Split the data on the newline character and create a dictionary
            temp = []
            for item in converted_data:
                info1, name = item.split("\n")
                temp.append(name)
            
        except NoSuchElementException:
            image_url = "Image Not Found"
            
        poster_list.append(image_url)
        info.append(temp)     
        #driver.close()
    driver.quit()
    return poster_list, info, plot
   