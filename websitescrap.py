from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import math
#import urllib
#import urllib.request
#from io import BytesIO
import io
from PIL import Image
import requests

url = 'https://www.' # website scrapper

########### CREATE THE FUNCTION clothes-scrapper to call later ##############

def cscrap(url):

    # create chrome instance
    driver = webdriver.Chrome(executable_path='/Users/ygeorgas/Desktop/other scrappers/chromedriver')

    driver.get(url)
    driver.maximize_window()

######################  setup the clicks to click the right pages to scrap ###################################
    # click out the shipping to UK disclaimer (if there is one shown)
    try:
        driver.find_element_by_xpath('//*[@id="firstVisitChangeCountryLayer"]/div[1]/button/span[2]').click()
    except:
        pass
    # click out the gift for you disclaimer (if there is one shown)
    try:
        driver.find_element_by_xpath('//*[@id="close_yi_box"]').click()
    except:
        pass
    # click the Clothing button
    driver.find_element_by_xpath('//*[@id="sections-menu"]/li[3]/span').click()

    #click the Shirts button (Main category clothes)
    element1 = driver.find_element_by_xpath('//*[@id="js-clothingwomen"]/div[1]/div/div[1]/div[2]/div[4]/a')
    driver.execute_script("arguments[0].click();", element1)
        #click the blouses button (subcategory of Shirts clothes)
    element2 = driver.find_element_by_xpath('//*[@id="teleyooxCategories"]/div[2]/div/ul/li[7]/div/ul/li[1]/a/span[2]')
    driver.execute_script("arguments[0].click();", element2)
    time.sleep(5)

###################  Scrapping page by page   ##################################################
    #lets find first how many pages we need to crawl
    totalpages = '//*[@id="navigation-bar-bottom"]/div[2]/ul/li[5]/a'
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, totalpages)))
    page_element = driver.find_element_by_xpath(totalpages)
    pages = int(page_element.text)
    print(pages, 'total number of pages found')
    # lets find how many photos are to understand how many products per page we can find.
    results_per_page = len(driver.find_elements_by_tag_name('img'))
    print(results_per_page, 'products per page')
    # so in total we should have approximately pages * results per page
    total_number_products = results_per_page * pages
    print(total_number_products, 'total number of products approximately')
    # lets now scrape a page - click to move to next page - scrape - next - scrape until we scrape all pages
    count = 0
    for page in range(pages-1):
        #find all images from page
        image_elements = driver.find_elements_by_tag_name('img')
        print(image_elements)
        for image_element in image_elements:
            try:
                # go to each image for the webpage to load (only then we can actually download it)
                actions = ActionChains(driver)
                actions.move_to_element(image_element).perform()
                # now get the src attribute from each image
                image_url = image_element.get_attribute("src")
                print('Receiving:', image_url)
                # Send an HTTP GET request, get and save the image from the response
                image_object = requests.get(image_url, timeout=5.0)
                with Image.open(io.BytesIO(image_object.content)) as im:
                    im.save('/Users/ygeorgas/Desktop/Other scrappers/YOOX/'+str(count)+'.jpg')
                count += 1
            #there might be a problem like no src found or the url is broken etc. We dont want the scrapper to blow up
            except:
                print('Error')

            #Now lets load the next results page by clicking the play button at the bottom of the page on the right
        load_next_page ="#navigation-bar-bottom > div.col-16-24 > ul > li.next-page > a > span"
        next_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, load_next_page)))
        next_page.click()
        time.sleep(5)
        #when we reach 17*120 each page = 2040 photos we break the process
        if page == 17:
            break
    driver.quit()
    return

#run the function
cscrap(url)

'''what is the meaning of arguments[0] here?
The execute_script() method has 2 parameters. The first is the script, the second is a vararg in which you
can place any parameters used in the script. In this case we only need the element as parameter, but since it is a
vararg our element is the first in the collection. For example you could also do driver.execute_script("arguments[0].click(); arguments[1].click();" element1, element2)
This would click both elements passed '''
