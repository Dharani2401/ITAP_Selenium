from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from keyboard import press
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
    driver.maximize_window()

    

    lines='//input[@name="blank"]'
    xpath_list.append('//input[@name="blank"]')
    value_list.append('sdgd')
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="blank"]')))
    classname_list.append(element.get_attribute("className"))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.clear()
    element.send_keys('sdgd')
    steps += "\n" + "test_step_inputsdgd"
    text_list.append(element.text)
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\json\\9\\page2.png')
    output['//input[@name="blank"]'] =  "sdgd"
    

    lines='//input[@name="email"]'
    xpath_list.append('//input[@name="email"]')
    value_list.append('ddfh')
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="email"]')))
    classname_list.append(element.get_attribute("className"))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.clear()
    element.send_keys('ddfh')
    steps += "\n" + "test_step_inputddfh"
    text_list.append(element.text)
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\json\\9\\page3.png')
    output['//input[@name="email"]'] =  "ddfh"
    
    xpath_list.append('page title')
    value_list.append('')
    text_list.append('')
    classname_list.append('')
    Title_element = driver.title
    steps="\n test_step_assert Page title is "+Title_element
    message+="\n Action Performed : The page title is "+Title_element
    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\json\\9\\page4.png')
                
    
    with open("D:\iTAP\Recorded_Scenarios\\json\\9\\logfile.log", "w+") as external_file:
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
    path = open("D:\iTAP\Recorded_Scenarios\\json\\9\\logfile.log", 'w+')
    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
    path.close()
    driver.close()