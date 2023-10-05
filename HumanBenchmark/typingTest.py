from selenium import webdriver
from pynput.keyboard import Key, Controller as KeyboardController
import time

keyboard = KeyboardController()

driver = webdriver.Chrome()

# Open a new tab and navigate to the URL
driver.execute_script("window.open('https://humanbenchmark.com/tests/typing', '_blank')")
driver.switch_to.window(driver.window_handles[-1])
driver.maximize_window()

# Wait for the page to load
time.sleep(10)

# Get the source code of the page
html = driver.page_source

# Find the paragraph
first = html.find('<span class="incomplete current">')
last = html.rfind('<span class="incomplete">')

# Parse the paragraph
paragraph = html[first:last+26].replace('<span class="incomplete current">', '').replace('<span class="incomplete">', '').replace('</span>', '')

print(paragraph)
print('\n')

keyboard.type(paragraph)

# Close the tab and the web driver
a = input('Apreta enter para terminar: ')
driver.close()
driver.quit()