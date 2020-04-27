#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import time
from splinter import Browser
from selenium import webdriver



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()

    # URL of page to be scraped - Scrape Nasa Mars News Site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Parse HTML with Beautiful Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Print article title and paragraph
    slide = soup.find('div', class_='list_text')
    news_title = slide.find('a').get_text()
    news_p = slide.find('div', class_='article_teaser_body').text


    # Image scrape
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Parse HTML with Beautiful Soup
    html = browser.html
    soup = bs(html, 'html.parser')


    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    # Go to 'FULL IMAGE'
    browser.click_link_by_partial_text('FULL IMAGE')

    # Go to 'more info'
    browser.click_link_by_partial_text('more info')

    # Parse HTML with Beautiful Soup
    html = browser.html
    image_soup = bs(html, 'html.parser')

    # Scrape the URL
    feat_img_url = image_soup.find('figure', class_='lede').a['href']
    featured_image_url = f'https://www.jpl.nasa.gov{feat_img_url}'





    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)

    import time
    time.sleep(2)

    # Parse HTML with Beautiful Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Tweet scrape
    tweet = soup.article.get_text()

    tweet == tweet





    # Visit Mars Facts page for facts about Mars
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    html = browser.html




    # Use Pandas to scrape the table containing facts about Mars
    table = pd.read_html(facts_url)
    mars_facts = table[1]
    # mars_facts

    # Drop Earth
    mars_df = mars_facts.drop(columns=['Earth'])

    # Rename Columns
    mars_df_renamed = mars_df.rename(columns={"Mars - Earth Comparison": "Description", "Mars": "Value"})
    # mars_df_renamed



    # Reset Index to be description
    mars_df_renamed.set_index('Description', inplace=True)
    # mars_df_renamed




    # Mars Hemispheres
    # Cerberus URL
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)

    # Parse HTML with Beautiful Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Image scrape
    cerberus_url = soup.find('div', class_='downloads')
    link = cerberus_url.find('a')
    cerberus_href = link['href']




    # Schiaparelli URL
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)

    # Parse HTML with Beautiful Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Image scrape 
    schia_url = soup.find('div', class_='downloads')
    link = schia_url.find('a')
    schia_href = link['href']



    # Syrtis Major URL
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)

    # Parse HTML with Beautiful Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Image scrape
    syrtis_url = soup.find('div', class_='downloads')
    link = syrtis_url.find('a')
    syrtis_href = link['href']



    # Valles Marineris URL
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)

    # Parse HTML with Beautiful Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    #Image url
    valles_url = soup.find('div', class_='downloads')
    link = valles_url.find('a')
    valles_href = link['href']



    # Library of hemisphere images

    hemisphere_image_urls = [
        {'title': 'Cerberus Hemisphere', 'img_url': cerberus_href},
        {'title': 'Schiaparelli Hemisphere', 'img_url': schia_href},
        {'title': 'Syrtis Major Hemisphere', 'img_url': syrtis_href},
        {'title': 'Valles Marineris Hemisphere', 'img_url': valles_href}
    ]



    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": tweet,
        "mars_facts": mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

if __name__ == '__main__':
    scrape()


