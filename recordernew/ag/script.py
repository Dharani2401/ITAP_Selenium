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
    driver.get("https://www.ag-grid.com/example/?gclid=Cj0KCQjw3IqSBhCoARIsAMBkTb1ACNzSha2uEfJ_OMD3GAN_N-6PFFU585evjR4M6ExekJUgqOrhry0aAlAtEALw_wcB")
    xpath_list.append('Open_Browser')
    value_list.append("https://www.ag-grid.com/example/?gclid=Cj0KCQjw3IqSBhCoARIsAMBkTb1ACNzSha2uEfJ_OMD3GAN_N-6PFFU585evjR4M6ExekJUgqOrhry0aAlAtEALw_wcB")
    classname_list.append('')
    text_list.append('')
    #friendly_names.append("Open Browser")
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\ag\\page1.png')
    driver.maximize_window()

    
    lines="step : 2"

    possible_xpaths=['//select[@id="data-size"]', '//select[@value="0.1x22"][contains(., "100 Rows, 22 Cols1000 Rows, 22 Cols10000 Rows, 100 Cols50000 Rows, 22 Cols100000 Rows, 22 Cols")]', '//select']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = Select(driver.find_element_by_xpath(i))
            element.select_by_value('1x22')
            o = element.first_selected_option
            output[i] =  "1x22"
            steps += "\n" + "test_step_select" + o.text
            break
        except:
             if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 2 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\ag\\page1.png')
    
    lines="step : 3"

    possible_xpaths=['//select[@id="grid-theme"]', '(//select)[2]', '(//select[contains(@type ,"select-one")])[2]']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = Select(driver.find_element_by_xpath(i))
            element.select_by_value('ag-theme-material')
            o = element.first_selected_option
            output[i] =  "ag-theme-material"
            steps += "\n" + "test_step_select" + o.text
            break
        except:
             if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 3 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\ag\\page2.png')
    
    lines="step : 4"

    possible_xpaths=['(//input)[10]', '(//input[contains(@class ,"ag-floating-filter-input")])[10]', '(//input[contains(@type ,"text")])[10]']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            input_type = element.get_attribute("type")
            if input_type.lower() == "search":
                for c in ('tony'):
                    element.send_keys(c)
                    time.sleep(3)
            else:
                element.send_keys('tony')
            output[i] =  "tony"
            steps += "\n" + "test_step_inputtony"
            break
        except:
             if len(possible_xpaths)-1 == idx:
                message+="\n Error : Execution stopped at step 4 ."
                raise Exception('Element Not Found')
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\ag\\page3.png')
    
    lines="step : 5"

    possible_xpaths=['//input[@id="ag-530-input"]', '(//input)[20]', '(//input[contains(@class ,"ag-input-field-input ag-checkbox-input")])[20]', '(//input[contains(@type ,"checkbox")])[20]', '(//input[contains(@ref ,"eInput")])[20]']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\ag\\page4.png')
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
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\ag\\page4.png')
                
    lines="step : 6"

    possible_xpaths=['//input[@id="ag-651-input"]', '(//input)[21]', '(//input[contains(@class ,"ag-input-field-input ag-checkbox-input")])[21]', '(//input[contains(@type ,"checkbox")])[21]', '(//input[contains(@ref ,"eInput")])[21]']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\ag\\page5.png')
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
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\ag\\page5.png')
                
    lines="step : 7"

    possible_xpaths=['//input[@id="ag-699-input"]', '(//input)[22]', '(//input[contains(@class ,"ag-input-field-input ag-checkbox-input")])[22]', '(//input[contains(@type ,"checkbox")])[22]', '(//input[contains(@ref ,"eInput")])[22]']
    for idx,i in enumerate(possible_xpaths):
        try:
            element = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, i)))
            driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\ag\\page6.png')
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
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\recordernew\\ag\\page6.png')
                
    
    with open("D:\iTAP\Recorded_Scenarios\\recordernew\\ag\\logfile.log", "w+") as external_file:
        finish_time = datetime.now()
        total = finish_time - start_time
        total=str(total).split(".")[0]
        final = "total time taken : " + total
        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list)  + "\n"+ final )
    print("test passed - no errors" + "\n" +steps + "\n"+message+ "\n"+ final )
    driver.close()
except Exception as e:
    print(e)
    finish_time = datetime.now()
    total = finish_time - start_time
    total=str(total).split(".")[0]
    path = open("D:\iTAP\Recorded_Scenarios\\recordernew\\ag\\logfile.log", 'w+')
    path.write("test case failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list)  +" \n total time taken : "+total)
    print("test case failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines+" \n total time taken : "+total)
    path.close()
    driver.close()
