
# Libraries
from splinter import Browser
from bs4 import BeautifulSoup
import time
import os, ssl
import pandas as pd
import pymongo


def init_browser():
    #Allow for site navigation
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    browser = init_browser()

    scraped_data = {}

# NASA

    # # Visit Nasa site
    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_url)
    time.sleep(2)
    
    # Grab site's html code and parse
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve desired data from code
    news_title = soup.find("div", class_='list_text').\
    find("div", class_="content_title").text

    news_paragraph = soup.find("div", class_='list_text').\
    find("div", class_="article_teaser_body").text

    scraped_data["news_title"] = news_title
    scraped_data["news_paragraph"] = news_paragraph
    scraped_data["nasa_url"] = nasa_url

# JPL

    jpl_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_image)
    time.sleep(2)

    # Grab site's html code and parse
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Visit link 
    browser.find_by_id("full_image").click()
    time.sleep(2)
    browser.click_link_by_partial_text("more info")

    # Grab site's html code and parse
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve desired data from code
    featured_image_url = soup.find(class_ = "lede").a['href']
    featured_image_url = f'https://www.jpl.nasa.gov{featured_image_url}'

    scraped_data["featured_image_url"] = featured_image_url
    scraped_data["jpl_image"] = jpl_image

# TWITTER

    #Visti Mars' weather tweet
    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_url)
    time.sleep(2)

    # Grab site's html code and parse
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve desired data from code
    tweet_text = soup.find("div", class_='css-1dbjc4n').\
    find("div", class_='css-901oao r-jwli3a r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').\
    find("span", class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0').text

    scraped_data["tweet_text"] = tweet_text

# FACTS
    #Visti Space Facts site
    mars_url = "https://space-facts.com/mars/"
    browser.visit(mars_url)
    time.sleep(2)

    # Grab site's html code and parse
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Generic code to allow read of html tables 

    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

    # Read html tables
    tables_df = pd.read_html(mars_url)[0]

    # Convert table to DF
    tables_df.columns = ["Description","Facts"]
    tables_df.set_index("Description", inplace = True)

    tables_html = tables_df.to_html()
    tables_html = tables_html.replace('\n', '')

    scraped_data["tables_html"] = tables_html


# HEMISPHERES

# ***Note***: The link provided appears to be broken. 
# Created a while loop to make sure the code runs for as long as it needs to
    hemisphere_image_urls = []

    while len(hemisphere_image_urls) == 0:

        #Visti Mars Facts site
        astrogeology_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(astrogeology_url)
        time.sleep(1)

        # Grab site's html code and parse
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")

        # Retrieve desired data from code
        products_list = soup.find_all("div", class_ = "item")


        # Create forloop to scrape images of Mars' hemispheres

        for result in products_list:
            title = result.find('h3').text
            partial_url = result.find('div', class_ = "description").a['href']
            full_url = f'https://astrogeology.usgs.gov{partial_url}'
            browser.visit(full_url)
            time.sleep(1)
            html = browser.html
            soup = BeautifulSoup(html, "html.parser")
            partial_image_url = soup.find('img', class_ = "wide-image")['src']
            full_image_url = f'https://astrogeology.usgs.gov{partial_image_url}'
            hemisphere_image_urls.append({'title':title, 'img_url':full_image_url})
        
    
    scraped_data["hemisphere_image_urls"] = hemisphere_image_urls

    # Close the browser after scraping
    browser.quit()

    # Return results
    return scraped_data