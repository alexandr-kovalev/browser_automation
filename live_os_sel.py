'''
This program changes the background of a webOS and adds a clock widget
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pathlib

PATH = pathlib.Path("G:\Code\Selenium_drivers\geckodriver\geckodriver-v0.31.0-win64")


driver = webdriver.Firefox(PATH)
driver.implicitly_wait(0.5)
driver.get("https://demo.os-js.org/")

desktop = '/html/body/div[1]/div/div'

time.sleep(3.5)

actions = ActionChains(driver)

def main():
    close_welcome_window()
    add_widget_clock()
    select_wallpaper()
    open_os_menu()


def close_welcome_window():
    wait_to_load('x_welcome_window', left_click, "/html/body/div[1]/div[2]/div/div[1]/div[5]")


def add_widget_clock():
    wait_to_load('desktop_menu', right_click, desktop)
    wait_to_load('add_widget', left_click, '/html/body/div[4]/div/ul/li[3]/div')
    wait_to_load('add_clock', left_click, '/html/body/div[4]/div/ul/li[3]/div/ul/li/div')


def select_wallpaper():
    wait_to_load('desktop_menu', right_click, '/html/body/div[1]/div[1]/div')
    wait_to_load('open_wallpaper', left_click, '//*[@id="osjs-context-menu"]/ul/li[1]/div')
    time.sleep(.5)
    wait_to_load('change_wallpaper', double_click, '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]')


def open_os_menu():
    wait_to_load('open_os_menu', left_click, '/html/body/div[5]/div[1]/div')


def right_click(element):
    actions.context_click(element)
    actions.perform()
    

def left_click(element):
    actions.click(element)
    actions.perform()


def double_click(element):
    actions.double_click(element)
    actions.perform()


def wait_to_load(name:str,func,xpath:str):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        func(element)
    finally:
        print(f'[+] Finished: {name}')



def type_text():
    pass


def input_keys(*args):
    if len(args) != 1:
        for arg in args:
            break
    pass



if __name__ == '__main__':
    main()
