from selenium import webdriver 
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

username = 'agora username'
password = 'agora password'
def go_to_page(br):
    #page_num = page_num - 1
    #start_results = page_num * 100
    #start_results = str(start_results)
    url = 'http://3g2upl4pq6kufc4m.onion'
    print ('[*] loading url: '+url)
    br.get(url)
    #br.get_screenshot_as_file('agora.tiff')
    usernamed = br.find_element_by_name("username")
    usernamed.send_keys(username) # password
    passwordd = br.find_element_by_name("password") # enterCaptcha
    passwordd.send_keys(password)
    captchad = br.find_element_by_name("enterCaptcha")
    capt = raw_input('enter captcha you see on screen: ')
    captchad.send_keys(capt)
    br.implicitly_wait(3)
    br.find_element_by_name("submit").click()

def start_browser():
    profiler = webdriver.FirefoxProfile('/Users/jc/Library/Application Support/Firefox/Profiles/dhzontsg.tor')
    br = webdriver.Firefox(firefox_profile=profiler)
    br.implicitly_wait(10)
    return br

def main():
    br = start_browser()
    go_to_page(br)

main()