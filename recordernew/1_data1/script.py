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
#friendly_names=[]
delay=5
    
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
    #friendly_names.append("Open Browser")
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\page1.png')
    driver.maximize_window()

    
    lines="step : 2"

    possible_xpaths=['//input[@name="user-name"]', '//input[@id="user-name"]', '//input[@placeholder="Username"]', '//input']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            input_type = element.get_attribute("type")
            if input_type.lower() == "search":
                for c in ('itrkrt'):
                    element.send_keys(c)
                    time.sleep(3)
            else:
                element.send_keys('itrkrt')
            output[i] =  "itrkrt"
            steps += "\n" + "test_step_inputitrkrt"
            break
        except:
             if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 2 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\page1.png')
    
    lines="step : 3"

    possible_xpaths=['//input[@name="password"]', '//input[@id="password"]', '//input[@placeholder="Password"]', '(//input)[2]', '(//input[contains(@class ,"input_error form_input")])[2]', '(//input[contains(@type ,"password")])[2]']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            input_type = element.get_attribute("type")
            if input_type.lower() == "search":
                for c in ('djtjtrj'):
                    element.send_keys(c)
                    time.sleep(3)
            else:
                element.send_keys('djtjtrj')
            output[i] =  "djtjtrj"
            steps += "\n" + "test_step_inputdjtjtrj"
            break
        except:
             if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 3 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\page2.png')
    
    lines="step : 4"

    possible_xpaths=['//input[@name="login-button"]', '//input[@id="login-button"]', '(//input)[3]', '(//input[contains(@class ,"submit-button btn_action")])[3]', '(//input[contains(@type ,"submit")])[3]']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\page3.png')
            output[i] = element.text
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            try:
                element.click()
            except Exception :
                driver.execute_script("arguments[0].click();", element)
            steps += "\n" +"test_step_click"
            break
        except:
            if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 4 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\page3.png')
                
    lines="step : 5"

    possible_xpaths=['//h4', '//h4,//h4[contains(., "Accepted usernames are:")]']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\page4.png')
            output[i] = element.text
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            try:
                element.click()
            except Exception :
                driver.execute_script("arguments[0].click();", element)
            steps += "\n" +"test_step_click"
            break
        except:
            if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 5 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\page4.png')
                
    lines="step : 6"

    possible_xpaths=['(//div)[3]', '(//div[contains(@class ,"login_logo")])[3]']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\page5.png')
            output[i] = element.text
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            try:
                element.click()
            except Exception :
                driver.execute_script("arguments[0].click();", element)
            steps += "\n" +"test_step_click"
            break
        except:
            if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 6 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\page5.png')
                
    lines="step : 7"

    possible_xpaths=['(//div)[11]', '(//div[contains(@class ,"bot_column")])[11]']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\page6.png')
            output[i] = element.text
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            try:
                element.click()
            except Exception :
                driver.execute_script("arguments[0].click();", element)
            steps += "\n" +"test_step_click"
            break
        except:
            if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 7 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\page6.png')
                
    
    with open("D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\logfile.log", "w+") as external_file:
        finish_time = datetime.now()
        total = finish_time - start_time
        total=str(total).split(".")[0]
        final = "total time taken : " + total
        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list)  + "\n"+ final )
    print("test passed - no errors" + "\n" +steps + "\n"+message+ "\n"+ final + "\nStart Time : " +str(start_time.strftime("%d/%m/%Y %H:%M:%S")))
    driver.close()
except Exception as e:
    print(e)
    finish_time = datetime.now()
    total = finish_time - start_time
    total=str(total).split(".")[0]
    path = open("D:\iTAP\Recorded_Scenarios\\recordernew\\1_data1\\logfile.log", 'w+')
    path.write("test case failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list)  +" \n total time taken : "+total)
    path.close()
    print("test case failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\nExecution stopped at : " +lines+"\ntotal time taken : "+total+ "\nStart Time : " +str(start_time.strftime("%d/%m/%Y %H:%M:%S")))
    driver.close()