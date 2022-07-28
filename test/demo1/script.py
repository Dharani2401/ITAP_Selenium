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
xpath_list=[]
value_list=[]
text_list=[]
classname_list=[]
lines=''
steps='' 
message=''
step_no=0
output_list = []
output = {}
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
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page1.png')
    driver.maximize_window()

    

    lines='//input[@name="user-name"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="user-name"]')))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.clear()
    element.send_keys('standard_user')
    steps += "\ntest_step_input " + 'standard_user'
    xpath_list.append('//input[@name="user-name"]')
    value_list.append('standard_user')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page2.png')
    output['//input[@name="user-name"]'] =  "standard_user"
    

    lines='//input[@name="password"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.clear()
    element.send_keys('secret_sauce')
    steps += "\ntest_step_input " + 'secret_sauce'
    xpath_list.append('//input[@name="password"]')
    value_list.append('secret_sauce')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page3.png')
    output['//input[@name="password"]'] =  "secret_sauce"
    

    lines='//input[@name="login-button"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="login-button"]')))
    if element.text == '':
        steps += "\ntest_step_click " + '//input[@name="login-button"]'
    else:        
        steps += "\ntest_step_click " + element.text
    xpath_list.append('//input[@name="login-button"]')
    value_list.append('')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page4.png')
    output['//input[@name="login-button"]'] = element.text
    try:
        element.click()
    except Exception :
        driver.execute_script("arguments[0].click();", element)
            

    lines='//button[@name="add-to-cart-sauce-labs-backpack"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-backpack"]')))
    if element.text == '':
        steps += "\ntest_step_click " + '//button[@name="add-to-cart-sauce-labs-backpack"]'
    else:        
        steps += "\ntest_step_click " + element.text
    xpath_list.append('//button[@name="add-to-cart-sauce-labs-backpack"]')
    value_list.append('')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page5.png')
    output['//button[@name="add-to-cart-sauce-labs-backpack"]'] = element.text
    try:
        element.click()
    except Exception :
        driver.execute_script("arguments[0].click();", element)
            

    lines='//button[@name="add-to-cart-sauce-labs-bike-light"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-bike-light"]')))
    if element.text == '':
        steps += "\ntest_step_click " + '//button[@name="add-to-cart-sauce-labs-bike-light"]'
    else:        
        steps += "\ntest_step_click " + element.text
    xpath_list.append('//button[@name="add-to-cart-sauce-labs-bike-light"]')
    value_list.append('')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page6.png')
    output['//button[@name="add-to-cart-sauce-labs-bike-light"]'] = element.text
    try:
        element.click()
    except Exception :
        driver.execute_script("arguments[0].click();", element)
            

    lines='//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    if element.text == '':
        steps += "\ntest_step_click " + '//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]'
    else:        
        steps += "\ntest_step_click " + element.text
    xpath_list.append('//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]')
    value_list.append('')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page7.png')
    output['//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]'] = element.text
    try:
        element.click()
    except Exception :
        driver.execute_script("arguments[0].click();", element)
            

    lines='//button[@id="react-burger-menu-btn"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
    if element.text == '':
        steps += "\ntest_step_click " + '//button[@id="react-burger-menu-btn"]'
    else:        
        steps += "\ntest_step_click " + element.text
    xpath_list.append('//button[@id="react-burger-menu-btn"]')
    value_list.append('')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page8.png')
    output['//button[@id="react-burger-menu-btn"]'] = element.text
    try:
        element.click()
    except Exception :
        driver.execute_script("arguments[0].click();", element)
            

    lines='//a[@id="about_sidebar_link"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="about_sidebar_link"]')))
    if element.text == '':
        steps += "\ntest_step_click " + '//a[@id="about_sidebar_link"]'
    else:        
        steps += "\ntest_step_click " + element.text
    xpath_list.append('//a[@id="about_sidebar_link"]')
    value_list.append('')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page9.png')
    output['//a[@id="about_sidebar_link"]'] = element.text
    try:
        element.click()
    except Exception :
        driver.execute_script("arguments[0].click();", element)
            
    xpath_list.append('page title')
    value_list.append('')
    classname_list.append('')
    text_list.append('')
    Title_element = driver.title
    steps="\ntest_step_assert Page title is "+Title_element
    message+="\n Action Performed : The page title is "+Title_element
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page10.png')
                
    
    with open("D:\iTAP\Recorded_Scenarios\\test\\demo1\\logfile.log", "w+") as external_file:
        finish_time = datetime.now()
        total = finish_time - start_time
        total=str(total).split(".")[0]
        final = "total time taken : " + total
        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
    driver.close()
except Exception as e:
    print(e)
    finish_time = datetime.now()
    total = finish_time - start_time
    total=str(total).split(".")[0]
    path = open("D:\iTAP\Recorded_Scenarios\\test\\demo1\\logfile.log", 'w+')
    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
    path.close()
    driver.close()