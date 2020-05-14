
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import bs4
import requests
import pyperclip
import webbrowser
from sys import argv


print("""
FOR THIS ONE COPY SOME OF THE TABLES FROM THE BOOK INTO ANKI DIRECTLY!!!
NOT DOING COREY NOW. WILL REDO WEB SCRAPING AFTER I LEARN A BIT MORE ABOUT THEWEB.
""")

# print("-------------------- WEBBROWSER --------------------")
# # open webpages
# webbrowser.open('https://inventwithpython.com/')
#
# # take the argument passed to the file
# if argv[1]:
#     address = argv[1]
# else:
#     # or read the clipboard if argument empty
#     address = pyperclip.paste()
#
# L = address.split(' ')
# s = '+'.join(L)
# webbrowser.open(f'https://www.google.com/maps/place/{s}')


# print("-------------------- REQUESTS --------------------")
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res))
#
# # we can check if the request succeeded
# res.status_code == requests.codes.ok  # variable with value 200
# print(res.status_code)  # 200
# print(len(res.text))  # 178k chars
# print(res.text[:1000])  # first 100 chars
#
# # a simpler way to check if the request succeeded is using this method
# # res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# res.raise_for_status()
# # NOTE: they say you should ALWAYS call raise_for_status after requests, to ensure download actually succeeded

# # we can save a page we downloaded as long as NOTE: we pass 'wb' = write bytes
# with open('saved_romeo_juliet.txt', 'wb') as f:
#     # here we're breaking our downloaded data into chunks to be writtern. Al said 100k is a good chunk size, so use it.
#     for chunk in res.iter_content(100_000):
#         f.write(chunk)


print("-------------------- BS4 --------------------")

# res = requests.get('https://www.weather.gov/')
# res.raise_for_status()
# print(res.text)
# weatherSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(weatherSoup))

# we can also use bs4 on a file we have stored locally
# with open('example.html', 'r') as f:
#     exampleSoup = bs4.BeautifulSoup(f, 'html.parser')
#     print(type(exampleSoup))

# we can use a faster parser than the built-in html.parser -> lxml parser - NOTE: it's an L not an i:)
# with open('example.html', 'r') as f:
#     exampleSoup = bs4.BeautifulSoup(f, 'lxml')
#     print(type(exampleSoup))

# lets actually get some stuff out of the selector
# elems = exampleSoup.select('#author')
# id = ('#author'), class = ('.class'), div = (div) / (div p) / (div > p), (example(type=button))

# because there was only one element market with the author tag, that's exactly what we got here
# print(type(elems))
# print(str(elems[0]))
# print(elems[0].getText())  # nice - looks inside the actual element and gets the actual text
# print(elems[0].attrs)

# pElems = exampleSoup.select('p')
# print(len(pElems))  # this time length is 3 - there are 3 p elements in the file
# print(str(pElems[0]))
# print(pElems[0].getText())
# print(str(pElems[1]))
# print(pElems[1].getText())
# print(str(pElems[2]))
# print(pElems[2].getText())
#
# weatherElems = weatherSoup.select('#myfcst-fcst')
# print(len(weatherElems))
# print(str(weatherElems[0]))
# print(weatherElems[0].getText())
# print(weatherElems[0].attrs)


# print("-------------------- SELENIUM --------------------")
# browser = webdriver.Chrome(executable_path='./chromeDriver/chromedriver')
# print(type(browser))
# browser.get('https://inventwithpython.com')

# broadly speaking there are 2 commands we can call here:
# find_element_* returns the first object to match the search
# find_elements_* returns a list of WebElement_* objects for every matching element
# examples:
# browser.find_elements_by_class_name(name) #finds elements with class "name"
# browser.find_elements_by_css_selector(selector)
# browser.find_elements_by_id(id)
# browser.find_elements_by_link_text(text) #links (<a> elements) that exactly match the text
# browser.find_elements_bypartial_link_text(text) #links (<a> elements) with partial match
# browser.find_elements_by_name(name)
# browser.find_elements_by_tag_name(name) #by tag "name"
# NOTE: except for very last, all other ones are case sensitive!

# lets find an element and print some attributes / methods
# try:
#     browser.get('https://inventwithpython.com')
#     elem = browser.find_element_by_class_name('cover-thumb')
#     print('Found <%s> element with that class name!' % (elem.tag_name))
#     print(elem.tag_name)  # img
#     # print(elem.get_attribute(name))
#     # print(elem.text)
#     # print(elem.clear())  # not a text elem so dont expect to work
#     print(elem.is_displayed())  # true
#     print(elem.is_enabled())  # true
#     print(elem.is_selected())  # false
#     print(elem.location)  # 125, 1546
# except:
#     print('was not able to find an element with that name!')


# lets click some links
# try:
#     browser.get('https://inventwithpython.com')
#     linkElem = browser.find_element_by_link_text('Read Online for Free')
#     print(type(linkElem))
#     linkElem.click()
# except:
#     print('oops no read oneline for free link available!')

# lets fill out some forms
# try:
#     browser.get('https://login.metafilter.com')
#     userElem = browser.find_element_by_id('user_name')
#     userElem.send_keys('1234')
#     pwElem = browser.find_element_by_id('user_pass')
#     pwElem.send_keys('1234')
#     pwElem.submit()
# except:
#     pass

# selenium has a module for keys that are impossible to type into a tring value
# we need to import it like this: from selenium.webdriver.common.keys import Keys
# then eg Keys.DOWN, Keys.UP, Keys.ENTER, Keys.TAB etc become available
# try:
#     browser.get('https://automatetheboringstuff.com/2e/chapter12/')
#     # this is the thing we're going to be manipulating - the main html tag
#     htmlElem = browser.find_element_by_tag_name('html')
#     htmlElem.send_keys(Keys.SPACE)
#     htmlElem.send_keys(Keys.SPACE)
#     htmlElem.send_keys(Keys.SPACE)
#     htmlElem.send_keys(Keys.SPACE)
# except:
#     pass

# other buttons av in selenium are:
# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()


# try:
#     amazon = browser.find_element_by_link_text('Amazon')
#     amazon.click()
#     time.sleep(5)
#     browser.back()
#     time.sleep(2)
#     browser.quit()
# except:
#     pass
