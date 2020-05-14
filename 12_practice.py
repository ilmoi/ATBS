# Practice Questions
# 1. Briefly describe the differences between the webbrowser, requests, bs4, and selenium modules.
# webbrowser - opens websites, requests - gets data from websites, bs4 - scrapes websites to find specific data, selenium - lets you simulate a user using a browser (for testing or else!)
# 2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?
# <class 'requests.models.Response'>
# access through .text
# 3. What requests method checks that the download worked?
# res.raise_for_status()
# 4. How can you get the HTTP status code of a requests response?
# res.status_code
# 5. How do you save a requests response to a file?
# with open() as f: for chunk in res.iter_content(100_000) f.write(chunk)
# 6. What is the keyboard shortcut for opening a browser’s developer tools?
# alt cmd i
# 7. How can you view (in the developer tools) the HTML of a specific element on a web page?
# right click > inspect element


# bs4 questions
# 8. What is the CSS selector string that would find the element with an id attribute of main?
# ok so a selector is nothing more than a "style" that applies to some elements
# selectors can target tag names (eg "body" or "head", "ul", "li ")
# selectors can target classes (you can then assign a bunch of "ul"s to a class) - in css you can define classes like section.feature-box and subclasses like section.feature-box.sales, section.feature-box.marketing etc
# selectors can target clases based on IDs. you can only have one of them per page
soup.select('#main')  # because ids are preceded with #!!

# 9. What is the CSS selector string that would find the elements with a CSS class of highlight?
soup.select('.highlight')  # because classes in css defined with a dot

# 10. What is the CSS selector string that would find all the <div> elements inside another <div> element?
soup.select('div')  # all divs
soup.select('div span')  # all spans within divs
soup.select('div > span')  # all spans DIRECTLY within divs

# 11. What is the CSS selector string that would find the <button> element with a value attribute set to favorite?
soup.select('favorite[type="button"]')
# this would be one that selects all elements named favorite with a "name" attribute with any value
soup.select('favorite[name]')

# 12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element <div>Hello, world!</div>. How could you get a string 'Hello, world!' from the Tag object?
spam[0].getText()

# 13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?
linkElem = spam[0].attrs
#
# 14. Running import selenium doesn’t work. How do you properly import the selenium module?
## from selenium.webdriver.common.keys import Keys
# from selenium import webdriver

# 15. What’s the difference between the find_element_* and find_elements_* methods?
# find element returns just one (first) object, elements returns all the objects it finds
#
# 16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?
browser.get(url)
linkElem = browser.find_element_by_link_text('Aamzon')
linkElem.click()

browser.get(url)
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.SPACE)
#
# 17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with selenium?
pwElem = browser.find_element_by_id('user_pass')
pwElem.send_keys('1234')
pwElem.send_keys(Keys.RETURN)  # OR
pwElem.submit()  # there's a special submit method
#
# 18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with selenium?
browser.forward()
browser.back()
browser.quit()
browser.refresh()
