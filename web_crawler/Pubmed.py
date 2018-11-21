#!/usr/bin/env python
# coding: utf-8

# Refrences
## https://mulder21c.github.io/2018/06/20/creating-web-crawler-in-python/
## http://hellogohn.com/post_one98
## https://medium.com/@nsh235482/python-selenium으로-웹사이트-크롤링하기-2-웹-사이트-제어해보기-1ffc5e05179d
## https://selenium-python.readthedocs.io/locating-elements.html
## T아카데미 - Python을 활용한 웹 크롤러 만들기

# pip 를 이용해서 라이브러리를 설치하기 전에 pip를 업데이트 합니다.
import sys
from IPython.display import Image #output 참고용 스크린샷 라이브러리 import
from selenium import webdriver #chrome을 실행시키기 위한 webdriver 라이브러리 import
from bs4 import BeautifulSoup as bs #웹크롤링을 위한 main 라이브러리 beautifulsoup를 import
from selenium.webdriver.support.ui import Select
import time

get_ipython().system('{sys.executable} -m pip install --upgrade pip')

# system을 통해서 실행하기 때문에 pip install beautifulsoup4가 아닌 앞에
# !{sys.executable} -m 이 붙게 됩니다.(consol에서 쓰는 -m도 붙어야 합니다.)
get_ipython().system('{sys.executable} -m pip install beautifulsoup4')
get_ipython().system('{sys.executable} -m pip install selenium')

options = webdriver.ChromeOptions() #크롬을 화면에 띄우지 않고 실행할 때 쓰는 코드(현재는 참고용으로만 적어놓음.)
options.add_argument('headless') #크롬을 화면에 띄우지 않고 실행할 때 쓰는 코드(현재는 참고용으로만 적어놓음.)

# replace 'chromedriver_path' with path where your chromedriver is located.
#driver = webdriver.Chrome('C:\\Users\\rucra\\Documents\\JupyterProject\\Crawling\\chromedriver', chrome_options=options) #chrome_options 부분에서 에러

# 크롬 드라이버를 먼저 설치한다.(설치 안하면 에러가 날 수도 있다.)
# https://sites.google.com/a/chromium.org/chromedriver/downloads
#driver = webdriver.Chrome('C:\\Users\\rucra\\Documents\\JupyterProject\\Crawling\\chromedriver') #설치한 chrome드라이버의 위치를 적는다.
driver = webdriver.Chrome('C:\\Users\\rucrazia\\Documents\\JupyterProject\\Crawling\\chromedriver') #설치한 chrome드라이버의 위치를 적는다.
driver.get("https://www.ncbi.nlm.nih.gov/pubmed") #실행하고 싶은 웹 페이지 url을 ""안에 적는다.
Image(driver.get_screenshot_as_png()) #실행된 화면을 캡쳐

#아래 pubmed가 켜지는 화면을 볼 수 있습니다.
driver = webdriver.Chrome('C:\\Users\\rucrazia\\Documents\\JupyterProject\\Crawling\\chromedriver') #설치한 chrome드라이버의 위치를 적는다.

driver.get("https://www.ncbi.nlm.nih.gov/pubmed") #실행하고 싶은 웹 페이지 url을 ""안에 적는다.

element = driver.find_element_by_id("term")
element.send_keys("epidemiology AND radiation AND non-cancer")

time.sleep(2) # 2초 무조건 대기
driver.find_element_by_id("search").click() #chrome 에서 search를 오른쪽 클릭하면 나오는 검사 버튼을 누르면 검사 버튼에 대한 id를 찾을 수 있다.
#pubmed의 search 버튼의 경우 chrome에서 찾으려고 하면 문제가 생길수도 있음. 필자는 windows edge로 찾았음. 크롬과 같은 방법으로 찾으나 '검사' 대신 '요소 검사'를 이용하는 것에서 차이점

time.sleep(2) # 무조건 대기
driver.find_element_by_id("sendto").click() #sento 버튼의 id

time.sleep(2) # 무조건 대기
driver.find_element_by_id("dest_File").click() #File 라디오 버튼의 id

time.sleep(1) # 무조건 대기
# select by visible text
select = Select(driver.find_element_by_id('file_format'))
for index in range(len(select.options)):
    select = Select(driver.find_element_by_id('file_format'))
    select.select_by_index(1)

time.sleep(2)

xpath_submit_button = "//button[@class='button_apply file ncbipopper-close-button']" #send to 안에 있는 Create File의 path를 추론하는 경로
driver.find_element_by_xpath(xpath_submit_button).click() #send to 안에 있는 Create File을 클릭

Image(driver.get_screenshot_as_png()) #실행된 화면을 캡쳐

