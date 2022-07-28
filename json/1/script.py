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
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\json\\1\\page1.png')
    driver.maximize_window()

    

    lines='//input[@name="user-name"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="user-name"]')))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.clear()
    element.send_keys('sdgdhfd')
    steps += "\ntest_step_input " + 'sdgdhfd'
    xpath_list.append('//input[@name="user-name"]')
    value_list.append('sdgdhfd')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\json\\1\\page2.png')
    output['//input[@name="user-name"]'] =  "sdgdhfd"
    

    lines='//input[@name="user-name"]'
    xpath1 =  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="user-name"]')))
    actions = ActionChains(driver)
    actions.move_to_element(xpath1).perform()
    xpath_list.append('//input[@name="user-name"]')
    value_list.append( '//input[@name="password"]')
    classname_list.append(xpath1.get_attribute("className"))
    text_list.append(xpath1.text)
    xpath1 = xpath1.text

    if xpath_list.__contains__('//input[@name="password"]'):
        xpath2=output['//input[@name="password"]']
    else:
        xpath2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
        xpath2 = xpath2.text
        output['//input[@name="password"]'] = xpath2
    if xpath1 == '' and xpath2 == '':
        steps += "\ntest_step_assert Assertion: "+ '//input[@name="password"]' +" not equal " + '//input[@name="user-name"]'
    else:        
        steps += "\ntest_step_assert Assertion: "+ xpath2 +" not equal " + xpath1
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\json\\1\\page3.png')
    output['//input[@name="user-name"]'] =  xpath1
    output['//input[@name="password"]'] = xpath2
    if not xpath1.lower().strip() == xpath2.lower().strip() :
         message+="\nAssertion Passed : expected text ["+xpath1+"] got text ["+xpath2+"] are not equal "
    else:
        message+="\nAssertion Failed : expected text ["+xpath1+"] got text ["+xpath2+"] are equal "
    

    lines='//input[@name="password"]'
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.clear()
    element.send_keys('ffgjf')
    steps += "\ntest_step_input " + 'ffgjf'
    xpath_list.append('//input[@name="password"]')
    value_list.append('ffgjf')
    classname_list.append(element.get_attribute("className"))
    text_list.append(element.text)
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\json\\1\\page4.png')
    output['//input[@name="password"]'] =  "ffgjf"
    
    lines='Assert multiple locators of class - //input[@name="login-button"] '
    a = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, '//input[@name="login-button"]')))
    xpath_list.append('//input[@name="login-button"]')
    value_list.append('')
    classname_list.append('')
    text_list.append('')
    value=''
    steps+="\ntest_step_assert Assert Multiple locators"
    if xpath_list.__contains__(''):
        value=output['']
    value=value.lower().strip()
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\json\\1\\page5.png')
    msg_count=0
    pass_count=0
    fail_count=0
    if len(a)>=1:
        for i in a:
            msg_count+=1
            if (i.text).lower().strip().__contains__(value):
                pass_count+=1
                message+='\n '+str(msg_count)+'. Assertion Passed : Expected [' + value + '] got ['+i.text+']'
            else:
                fail_count+=1
                message+='\n '+str(msg_count)+'. Assertion Failed : Expected [' + value + '] got ['+i.text+']'
    else:
        message+='\n Action Performed : No records found , while validating for [' + value + ']'
    message+="\n Action Performed : Passed Assertions ["+str(pass_count)+"] , Failed Assertions ["+str(fail_count)+"]"
        
    
    with open("D:\iTAP\Recorded_Scenarios\\json\\1\\logfile.log", "w+") as external_file:
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
    path = open("D:\iTAP\Recorded_Scenarios\\json\\1\\logfile.log", 'w+')
    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
    path.close()
    driver.close()