from selenium import webdriver
import time
import chromedriver_binary
from bs4 import BeautifulSoup
import urllib.request as req

def wether_url(ad):
    url = "https://tenki.jp/"
    address = ad
    driver = webdriver.Chrome()
    driver.get(url)
    element = driver.find_element_by_id("keyword")
    element.clear
    element.send_keys(address)
    button = driver.find_element_by_id("btn")
    button.click()
    n_button = driver.find_element_by_class_name("search-entry-data")
    n_button.click()
    c_url = driver.current_url
    return c_url

def get_temp(url_w):
    url = url_w
    max_low = []
    response = req.urlopen(url)
    p_html = BeautifulSoup(response, "html.parser") 
    span_list = p_html.find_all("span")
    max_low_tmp=[span_list[16],span_list[18]]
    for i in max_low_tmp:
        max_low.append(i.string)
    return max_low