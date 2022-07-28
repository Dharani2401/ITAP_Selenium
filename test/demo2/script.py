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
    driver.get("https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/")
    xpath_list.append('Open_Browser')
    value_list.append("https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/")
    classname_list.append('')
    text_list.append('')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page1.png')
    driver.maximize_window()

    

    lines='//input[@name="firstname"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="firstname"]')))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.clear()
    element.send_keys('sdgds')
    steps += "\ntest_step_input " + 'sdgds'
    xpath_list.append('//input[@name="firstname"]')
    value_list.append('sdgds')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page2.png')
    output['//input[@name="firstname"]'] =  "sdgds"
    

    lines='//input[@name="email"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="email"]')))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.clear()
    element.send_keys('sgds')
    steps += "\ntest_step_input " + 'sgds'
    xpath_list.append('//input[@name="email"]')
    value_list.append('sgds')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page3.png')
    output['//input[@name="email"]'] =  "sgds"
    

    lines='//input[@name="checkbox2"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="checkbox2"]')))
    if element.text == '':
        steps += "\ntest_step_click " + '//input[@name="checkbox2"]'
    else:        
        steps += "\ntest_step_click " + element.text
    xpath_list.append('//input[@name="checkbox2"]')
    value_list.append('')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page5.png')
    output['//input[@name="checkbox2"]'] = element.text
    try:
        element.click()
    except Exception :
        driver.execute_script("arguments[0].click();", element)
            

    lines='(//input[@name="B"])[2]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//input[@name="B"])[2]')))
    if element.text == '':
        steps += "\ntest_step_click " + '(//input[@name="B"])[2]'
    else:        
        steps += "\ntest_step_click " + element.text
    xpath_list.append('(//input[@name="B"])[2]')
    value_list.append('')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page6.png')
    output['(//input[@name="B"])[2]'] = element.text
    try:
        element.click()
    except Exception :
        driver.execute_script("arguments[0].click();", element)
            

    lines='(//input[@name="C"])[3]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//input[@name="C"])[3]')))
    if element.text == '':
        steps += "\ntest_step_click " + '(//input[@name="C"])[3]'
    else:        
        steps += "\ntest_step_click " + element.text
    xpath_list.append('(//input[@name="C"])[3]')
    value_list.append('')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page7.png')
    output['(//input[@name="C"])[3]'] = element.text
    try:
        element.click()
    except Exception :
        driver.execute_script("arguments[0].click();", element)
            

    lines='//select[@name="Listbox1"]'
    element = Select(driver.find_element_by_xpath('//select[@name="Listbox1"]'))
    element.select_by_value('GTK2 Port')
    o = element.first_selected_option
    if o.text == '':
        steps += "\ntest_step_click " + '//select[@name="Listbox1"]'
    else:        
        steps += "\ntest_step_click " + o.text
    xpath_list.append('//select[@name="Listbox1"]')
    value_list.append('GTK2 Port')
    classname_list.append('')
    text_list.append(o.text)
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page8.png')
    output['//select[@name="Listbox1"]'] =  "GTK2 Port"
    
    
    with open("D:\iTAP\Recorded_Scenarios\\test\\demo2\\logfile.log", "w+") as external_file:
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
    path = open("D:\iTAP\Recorded_Scenarios\\test\\demo2\\logfile.log", 'w+')
    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
    path.close()
    driver.close()