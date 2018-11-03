# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 11:49:31 2018

@author: LeeYipFung
"""

#test bot
from selenium import webdriver
from selenium.webdriver.common.by import By
# Using Chrome to access web
driver =webdriver.Chrome('C:/Users/LeeYipFung/Desktop/chromedriver')
# Open the website
driver.get('https://postcode.my/')

# Select the id box
location_box = driver.find_element_by_name('keyword')
# Equivalent Outcome! 
state_box = driver.find_element_by_name('state')
search_button=driver.find_element_by_id('submit_search')


location_box.send_keys('Tmn Nesa')
state_box.send_keys('Johor')
search_button.click()

driver.set_page_load_timeout(5)
try:
    table_id = driver.find_element(By.ID, 't2')
    rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
    size=len(rows)
    result=rows[size-1].find_elements(By.TAG_NAME, "td")[3] 
    print("Post code:"+result.text)
except:
    print("\n")