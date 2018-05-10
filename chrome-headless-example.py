from selenium import webdriver

#set a headless browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.instagram.com/jamesanthonycampbell/')
print(driver.title)
#print(driver.executeScript('window._sharedData.entry_data.ProfilePage[0].graphql.user.id'))
#print(driver._sharedData.entry_data.ProfilePage[0].graphql.user.id)
#print(driver.console.dir("window._sharedData.entry_data.ProfilePage[0].graphql.user.id"))
# element = driver.execute_script("return $(window._sharedData.entry_data.ProfilePage[0].graphql.user.id)") # doesn't work but maybe close?
# print(element)