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
    driver.get("https://demoqa.com/text-box")
    xpath_list.append('Open_Browser')
    value_list.append("https://demoqa.com/text-box")
    classname_list.append('')
    text_list.append('')
    #friendly_names.append("Open Browser")
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\demoqa\\page1.png')
    driver.maximize_window()

    
    lines="step : 2"

    possible_xpaths=['//input[@id="userName"]', '//input[@placeholder="Full Name"]', '//input']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            input_type = element.get_attribute("type")
            if input_type.lower() == "search":
                for c in ('fhfd'):
                    element.send_keys(c)
                    time.sleep(3)
            else:
                element.send_keys('fhfd')
            output[i] =  "fhfd"
            steps += "\n" + "test_step_inputfhfd"
            break
        except:
             if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 2 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\demoqa\\page1.png')
    
    lines="step : 3"

    possible_xpaths=['//input[@id="userEmail"]', '//input[@placeholder="name@example.com"]', '(//input)[2]', '(//input[contains(@class ,"mr-sm-2 form-control")])[2]', '(//input[contains(@type ,"email")])[2]']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            input_type = element.get_attribute("type")
            if input_type.lower() == "search":
                for c in ('ffdjj'):
                    element.send_keys(c)
                    time.sleep(3)
            else:
                element.send_keys('ffdjj')
            output[i] =  "ffdjj"
            steps += "\n" + "test_step_inputffdjj"
            break
        except:
             if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 3 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\demoqa\\page2.png')
    
    lines="step : 4"
    time.sleep(1)
                    
    lines="step : 5"

    message+='\n <-- STEP 5 MESSAGE --> '
    possible_xpaths=['text-field-containerselect_separatorinput']
    for idx,item in enumerate(possible_xpaths):
        try:
            name = item.split('select_separator')
            i = name[0]
            i=i.replace(' ','.')
            element1 = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME,i)))
            for i in element1:
                result1 = i.find_elements_by_tag_name(name[1])
            count1 = str(len(result1))
            element2 = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'text-field-container')))
            for j in element2:
                result2 = j.find_elements_by_tag_name('textarea')
            count2 = str(len(result2))
            if count1 == count2:
                message+="\nAssertion Passed : expected count ["+count1+"] equal to ["+count2+"]"
            else:
                message+="\nAssertion Failed : expected count ["+count1+"] not equal to ["+count2+"]"
            steps+="\n test_step_assert Find parent child count"
            driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\demoqa\\page4.png')
            break
        except:
            if len(possible_xpaths)-1 == idx:
                raise Exception('Element Not Found')
    
    lines="step : 6"

    possible_xpaths=['//textarea[@id="currentAddress"]', '//textarea[@placeholder="Current Address"]', '//textarea']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            input_type = element.get_attribute("type")
            if input_type.lower() == "search":
                for c in ('ffjfgkg'):
                    element.send_keys(c)
                    time.sleep(3)
            else:
                element.send_keys('ffjfgkg')
            output[i] =  "ffjfgkg"
            steps += "\n" + "test_step_inputffjfgkg"
            break
        except:
             if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 6 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\demoqa\\page5.png')
    
    lines="step : 7"

    possible_xpaths=['//textarea[@id="permanentAddress"]', '(//textarea)[2]', '(//textarea[contains(@class ,"form-control")])[2]', '(//textarea[contains(@type ,"textarea")])[2]']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            input_type = element.get_attribute("type")
            if input_type.lower() == "search":
                for c in ('fjfjfg'):
                    element.send_keys(c)
                    time.sleep(3)
            else:
                element.send_keys('fjfjfg')
            output[i] =  "fjfjfg"
            steps += "\n" + "test_step_inputfjfjfg"
            break
        except:
             if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 7 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\demoqa\\page6.png')
    
    lines="step : 8"
    message+='\n <-- STEP 8 MESSAGE --> '
    possible_xpaths=['menu-list']
    for idx,i in enumerate(possible_xpaths):
        try:
            i=i.replace(' ','.')
            element = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, i)))
            count1 = len(element1)
            element2 = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'text-field-container')))
            count2 = len(element2)
            steps+="\n test_step_assert Find all elements"
            driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\demoqa\\page7.png')
            if count1 == count2:
                message+="\nAssertion Passed : expected count ["+count1+"] equal to ["+count2+"]"
            else:
                message+="\nAssertion Failed : expected count ["+count1+"] not equal to ["+count2+"]"
            break
        except:
            if len(possible_xpaths)-1 == idx:
                message+='\nError : Element not found'  
        
        
    
    with open("D:\iTAP\Recorded_Scenarios\\recordernew\\demoqa\\logfile.log", "w+") as external_file:
        finish_time = datetime.now()
        total = finish_time - start_time
        total=str(total).split(".")[0]
        final = "total time taken : " + total
        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list)  + "\n"+ final )
    print("test passed - no errors", message)
    driver.close()
except Exception as e:
    print(e)
    finish_time = datetime.now()
    total = finish_time - start_time
    total=str(total).split(".")[0]
    path = open("D:\iTAP\Recorded_Scenarios\\recordernew\\demoqa\\logfile.log", 'w+')
    path.write("test case failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list)  +" \n total time taken : "+total)
    print("test case failed: ", message)
    path.close()
    driver.close()
