from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import date, datetime

xpath_list = []
value_list = []
text_list = []
classname_list = []
output_list = []
output = {}
lines = ''
steps = ''
message = ''
step_no = 0
try:
    start_time = datetime.now()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logger"])
    driver = webdriver.Chrome(options=options, executable_path='D:\iTAP\chromedriver.exe')
    driver.get("https://www.saucedemo.com/")
    xpath_list.append('Open_Browser')
    value_list.append("https://www.saucedemo.com/")
    classname_list.append('')
    text_list.append('')
    driver.maximize_window()

    driver.implicitly_wait(20)
    lines = '//input[@name="user-name"]'
    xpath_list.append('//input[@name="user-name"]')
    value_list.append('sdgdhfd')
    element = driver.find_element_by_xpath('//input[@name="user-name"]')
    classname_list.append(element.get_attribute("className"))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.clear()
    element.send_keys('sdgdhfd')
    steps += "\n" + "test_step_inputsdgdhfd"
    text_list.append(element.text)
    output = {'//input[@name="user-name"]': element.text}
    output_list.append(output)
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\json\\1\\page1.png')

    driver.implicitly_wait(20)
    lines = '//input[@name="user-name"]'
    xpath_list.append('//input[@name="user-name"]')
    value_list.append('sfdsf')
    xpath1 = driver.find_element_by_xpath('//input[@name="user-name"]')
    classname_list.append(xpath1.get_attribute("className"))
    actions = ActionChains(driver)
    actions.move_to_element(xpath1).perform()
    xpath1 = xpath1.text.lower().strip()
    text_list.append(xpath1)
    steps += "\n" + "test_step_input" + xpath1
    output['//input[@name="user-name"]'] = xpath1
    print(output)
    output_list.append(output)
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\json\\1\\page1.png')
    if xpath1 == 'sfdsf':
        message += '\nAssertion Passed : expected text [' + xpath1 + '] got text [sfdsf] are equal '
    else:
        message += '\nAssertion Failed : expected text [' + xpath1 + '] got text [sfdsf] are not equal '

    driver.implicitly_wait(20)
    lines = '//input[@name="password"]'
    xpath_list.append('//input[@name="password"]')
    value_list.append('ffgjf')
    element = driver.find_element_by_xpath('//input[@name="password"]')
    classname_list.append(element.get_attribute("className"))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.clear()
    element.send_keys('ffgjf')
    steps += "\n" + "test_step_inputffgjf"
    text_list.append(element.text)
    output = {'//input[@name="password"]': element.text}
    output_list.append(output)
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\json\\1\\page2.png')

    driver.implicitly_wait(20)
    lines = '//input[@name="login-button"]'
    xpath_list.append('//input[@name="login-button"]')
    value_list.append('')
    element = driver.find_element_by_xpath('//input[@name="login-button"]')
    classname_list.append(element.get_attribute("className"))
    steps += "\n" + "test_step_click" + element.text
    output = {'//input[@name="login-button"]': element.text}
    output_list.append(output)
    text_list.append(element.text)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\json\\1\\page3.png')
    driver.execute_script("arguments[0].click();", element)

    with open("D:\iTAP\Recorded_Scenarios\\json\\1\\logfile.log", "w+") as external_file:
        finish_time = datetime.now()
        total = finish_time - start_time
        total = str(total).split(".")[0]
        final = "total time taken : " + total
        external_file.write("Test passed - no errors" + "\n" + steps + "\n" + message + "\nxpath list " + str(
            xpath_list) + "\nvalue list " + str(value_list) + "\nclass name list " + str(
            classname_list) + "\ntext list " + str(text_list) + "\n" + final)
    driver.close()
except Exception as e:
    print(e)
    finish_time = datetime.now()
    total = finish_time - start_time
    total = str(total).split(".")[0]
    path = open("D:\iTAP\Recorded_Scenarios\\json\\1\\logfile.log", 'w+')
    path.write("Test case failed:" + str(
        e) + '\n' + steps + "\n" + message + "\nExecution stopped at : " + lines + "\nxpath list " + str(
        xpath_list) + "\nvalue list " + str(value_list) + "\nclass name list " + str(
        classname_list) + "\ntext list " + str(text_list) + " \nTotal time taken : " + total)
    path.close()
    driver.close()