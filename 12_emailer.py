from selenium import webdriver
import time

# basic, pick a browser navigate to main page
browser = webdriver.Chrome(executable_path='./chromeDriver/chromedriver')
browser.get('https://protonmail.com/')

# wait to load > click log in
time.sleep(1)
loginElem = browser.find_element_by_link_text('LOG IN')
loginElem.click()

# wait to load, login
time.sleep(1)
userElem = browser.find_element_by_id('username')
userElem.send_keys('')
pwElem = browser.find_element_by_id('password')
pwElem.send_keys('')
pwElem.submit()

# REAL FUCKING IMPORTANT. I SPENT 2 HOURS DEBUGGING THIS SHIT. YOU NEED TO ALLOW ENOUGH TIME FOR THE PAGE TO LOAD OR NONE OF THE BELOW WILL WORK.
time.sleep(3)
# HERE'S THE SYNTAX FOR THE BUTTON
# <button
# class="compose pm_button sidebar-btn-compose"
# action-compose=""
# action-compose-type="new"
# translate-context="Action"
# translate=""
# translate-comment="compose button in sidebar"
# >Compose</button>
# WORKS
composeElem = browser.find_element_by_xpath(
    "//button[@class='compose pm_button sidebar-btn-compose']")
# DOES NOT. NOT SURE WHY.
# composeElem = browser.find_element_by_link_text('Compose')
# composeElem = browser.find_element_by_class_name('compose pm_button sidebar-btn-compose')
composeElem.click()

# wait, enter who to sent to, email
time.sleep(2)
# <input id="autocompleteptq5b6vph9tq-1587638945334"
# name="autocomplete"
# autofocus=""
# autocomplete="off"
# spellcheck="false"
# autocapitalize="off"
# class="autocompleteEmails-input no-outline"
# aria-owns="awesomplete_list_2"
# role="combobox"
# aria-activedescendant="_item_0">
# WORKS
toElem = browser.find_element_by_xpath(
    "//input[contains(@id,'autocomplete')]")
# DOES NOT WORK - THE NUMBER AT THE END IS DIFFERENT EVERY TIME YOU LOAD THE PAGE, SO HE CANT FIND IT.
# toElem = browser.find_element_by_id('autocompleteptaehogmunqp-1587631238089')
toElem.send_keys('x')

# enter subject
time.sleep(2)
# <input title-translate-context="info" class="flex subject no-outline ng-pristine ng-empty ng-invalid ng-invalid-required ng-touched" placeholder-translate-context="Placeholder" ng-model="message.Subject" required="" placeholder="Subject" title="Subject">
# WORKS
subjectElem = browser.find_element_by_xpath("//input[@placeholder='Subject']")
# DOES NOT WORK
# subjectElem = browser.find_element_by_class_name(
#     'flex subject no-outline ng-pristine ng-empty ng-invalid ng-invalid-required ng-touched')
subjectElem.send_keys('coronavirus is a scam')

# hit the send button!
time.sleep(2)
# WORKS
sendElem = browser.find_element_by_xpath(
    "//button[@class='pm_button primary mobileFull composer-btn-send btnSendMessage-btn-action']")
# DOES NOT WORK
# sendElem = browser.find_element_by_link_text('Send')
sendElem.click()

# quit the browser, if everything went through successfully!
time.sleep(3)
browser.quit()
