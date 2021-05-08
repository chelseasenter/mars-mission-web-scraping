import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
executable_path = {'executable_path': ChromeDriverManager().install()}

def scrape_all():
    mars = {}
    browser = Browser("chrome", **executable_path, headless=False)

    browser.visit('https://mars.nasa.gov/news/')
    mars['title'] = browser.find_by_css('div.content_title a').text
    mars['paragraph'] = browser.find_by_css('div.article_teaser_body').text

    browser.visit('https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html')
    mars['image'] = browser.find_by_css('a.showimg')['href']

    mars['facts'] = pd.read_html('https://space-facts.com/mars/')[0].to_html()

    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')

    links = browser.find_by_css('a.itemLink h3')
    hemispheres = []
    for i in range(len(links)):
        hemisphere = {}
        hemisphere['title'] = browser.find_by_css('a.itemLink h3')[i].text
        browser.find_by_css('a.itemLink h3')[i].click()
        hemisphere['url'] = browser.find_by_text('Sample')['href']
        hemispheres.append(hemisphere)
        browser.back()
    browser.quit()
    mars['hemispheres'] = hemispheres
    
    return mars



