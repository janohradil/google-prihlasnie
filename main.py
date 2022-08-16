# from selenium_browsers_drivers import geckodiver as FirefoxDriverManager
from getpass import getpass

from selenium import webdriver
from selenium.webdriver.common.by import By

PATH_TO_DRIVER = './selenium_browsers_drivers/geckodriver'
IMPLICITLY_WAIT_TIME = 10

def google_login_selenium():
    try:
        driver = webdriver.Firefox(executable_path=PATH_TO_DRIVER)
        gmail_id = input('Zadaj svoj email do Google-u: ')
        gmail_pwd = getpass('Zadaj svoje heslo: ')
        url = 'https://accounts.google.com/signin/v2'

        driver.get(url)
        driver.implicitly_wait(IMPLICITLY_WAIT_TIME)

        login_box = driver.find_element(by=By.XPATH,
                                        value='//*[@id="identifierId"]')
        login_box.clear()
        login_box.send_keys(gmail_id)

        next_button = driver.find_element(by=By.ID, value='identifierNext')
        next_button.click()

        passwd_box = driver.find_element(by=By.XPATH,
                                         value='//*[@id ="password"]/div[1]/div / div[1]/input')
        passwd_box.clear()
        passwd_box.send_keys(gmail_pwd)

        next_button = driver.find_element(by=By.XPATH,
                                          value='//*[@id ="passwordNext"]')
        next_button.click()
        print('Úspešné prihlásenie do Google účtu. :)')
    except:
        print('Neúspešný pokus o prihlásenie do Google účtu :(')


if __name__ == '__main__':
    google_login_selenium()
