#print("Hello")
#def function1():
    #print("bye")
#function1()

import datetime
import time

def function():
    from selenium import webdriver
    global driver
    driver = webdriver.Chrome()
    driver.get('http://test-vm4:8080/login')
    print('VNMS page opened')
    username = driver.find_element_by_id("userTextBox").send_keys('admin@example.com')
    password = driver.find_element_by_id("login-pass").send_keys('vectastar')
    print('user name and password entered')
    login = driver.find_element_by_xpath("//button[@name='login']").click()
    print('page login')
    driver.implicitly_wait(10)
    button1 = driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
    print('click on Dashboard')
    button2 = driver.find_element_by_xpath("//span[contains(text(),'Inventory')]").click()
    print('click on Inventory')

#def function1():
    #button2 = driver.find_element_by_xpath("//span[contains(text(),'Inventory')]").click()
    #print('click on Inventory')

#####Function to show Page load time for limeklin_rc1

def function2():
    function()
    #function1()
    button3 = driver.find_element_by_xpath("//a[contains(text(),'limekiln_rc1')]").click()
    print('click on RC ')
    button4 = driver.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
    print('Select the Report option')
    button5 = driver.find_element_by_xpath("//span[@class='filter-option pull-left']").click()
    print('Report duration button selected')
    start1 = datetime.datetime.now()
    button6 = driver.find_element_by_xpath("//span[@class='filter-option pull-left'][contains(text(),'Last 1 Day')]")
    print('check if last 1 day option is selected')
    if not button6:
        print("No button6 found")
    else:
        print("button6 found")
    button7 = driver.find_element_by_class_name('overlay')
    if not button6:
        print("graph not found")
    else:
        print("graph found")
    timeout = time.time() + 60 * 1
    while len(driver.find_elements_by_css_selector("path[class='area areaChart']")) != 16:
        time.sleep(0.1)
        if time.time() > timeout:
            break
    elapsed1 = datetime.datetime.now()
    print("Elapsed Time1 = {0}".format(elapsed1 - start1))
    start2 = datetime.datetime.now()
    button8 = driver.find_element_by_xpath("//span[contains(text(),'Last Week')]").click()
    timeout = time.time() + 60 * 2
    while len(driver.find_elements_by_css_selector("path[class='area areaChart']")) != 16:
        time.sleep(0.1)
        if time.time() > timeout:
            break
    print('Last week option selected')
    elapsed2 = datetime.datetime.now()
    print("Elapsed Time2 = {0}".format(elapsed2 - start2))
    button5 = driver.find_element_by_xpath("//span[@class='filter-option pull-left']").click()
    start3 = datetime.datetime.now()
    button9 = driver.find_element_by_xpath("//span[contains(text(),'Last Month')]").click()
    timeout = time.time() + 60 * 2
    while len(driver.find_elements_by_css_selector("path[class='area areaChart']")) != 16:
        time.sleep(0.1)
        if time.time() > timeout:
             break
    print('Last month option selected')
    elapsed3 = datetime.datetime.now()
    end3 = (elapsed3 - start3).total_seconds()
    print("Elapsed_Time3 = {0}".format(elapsed3 - start3))
    assert  end3 <= 5,"Something has changed!"
    driver.close()

#####Function to show Page load time for LKH 12G West (H)

def function3():
    function()
    #function1()
    button3 = driver.find_element_by_xpath("//tr[@class='even']//span[@class='glyphicon glyphicon-chevron-right inventoryIcon']").click()
    print('drop down on Limekliln_rc2 ')
    button4 = driver.find_element_by_xpath("//a[contains(text(),'LKH 12G West (H)')]").click()
    print('AP selected')
    button5 = driver.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
    print('Select the Report option')
    button6 = driver.find_element_by_xpath("//span[@class='filter-option pull-left']").click()
    print('Report duration button selected')
    start1 = datetime.datetime.now()
    button7 = driver.find_element_by_xpath("//span[@class='filter-option pull-left'][contains(text(),'Last 1 Day')]")
    start1 = datetime.datetime.now()
    button8 = driver.find_element_by_partial_link_text("Last 1 Day")
    if not button8:
        print("No button8 found")
    else:
        print("button8 found")

    button9 = driver.find_element_by_class_name('overlay')
    if not button8:
        print("graph not found")
    else:
        print("graph found")
    timeout = time.time() + 60 * 1
    while len(driver.find_elements_by_css_selector("path[class='area areaChart']")) != 9:
        time.sleep(0.1)
        if time.time() > timeout:
            break
    elapsed1 = datetime.datetime.now()
    print("Elapsed Time1 = {0}".format(elapsed1 - start1))
    start2 = datetime.datetime.now()
    button8 = driver.find_element_by_xpath("//span[contains(text(),'Last Week')]").click()
    timeout = time.time() + 60 * 2
    while len(driver.find_elements_by_css_selector("path[class='area areaChart']")) != 9:
        time.sleep(0.1)
        if time.time() > timeout:
            break
    print('Last week option selected')
    elapsed2 = datetime.datetime.now()
    print("Elapsed Time2 = {0}".format(elapsed2 - start2))


    button5 = driver.find_element_by_xpath("//span[@class='filter-option pull-left']").click()
    start3 = datetime.datetime.now()
    button10 = driver.find_element_by_xpath("//span[contains(text(),'Last Month')]").click()

    timeout = time.time() + 60 * 2
    while len(driver.find_elements_by_css_selector("path[class='area areaChart']")) != 9:
        time.sleep(0.1)
        if time.time() > timeout:
            break
    print('Last month option selected')
    elapsed3 = datetime.datetime.now()
    end3 = (elapsed3 - start3).total_seconds()
    print("Elapsed Time3 = {0}".format(elapsed3 - start3))
    assert end3 <= 5, "Something has changed!"
    driver.close()

#####Function to show Page load time for John Easy

def function4():
    function()
    #function1()

    button3 = driver.find_element_by_xpath(
        "//tr[@class='even']//span[@class='glyphicon glyphicon-chevron-right inventoryIcon']").click()
    print('drop down on Limekliln_rc2 ')

    button4 = driver.find_element_by_xpath("//tr[@class='children']//tr[3]//td[1]//span[1]").click()
    print('drop_down on LKH 12G West (H) ')

    button5 = driver.find_element_by_xpath("//a[contains(text(),'John Easy')]").click()
    print('Select the John Easy option')

    button6 = driver.find_element_by_xpath("//a[@id='reports']").click()
    print('Select the Report option')

    button7 = driver.find_element_by_xpath("//span[@class='filter-option pull-left']").click()
    print('Report duration button selected')

    start1 = datetime.datetime.now()
    button8 = driver.find_element_by_partial_link_text("Last 1 Day")
    if not button8:
        print("No button8 found")
    else:
        print("button8 found")

    button9 = driver.find_element_by_class_name('overlay')
    if not button8:
        print("graph not found")
    else:
        print("graph found")

    elapsed1 = datetime.datetime.now()
    print("Elapsed Time1 = {0}".format(elapsed1 - start1))
    start2 = datetime.datetime.now()

    button10 = driver.find_element_by_xpath("//span[contains(text(),'Last Month')]").click()

    timeout = time.time() + 60 * 2
    while len(driver.find_elements_by_css_selector("path[class='area areaChart']")) != 19:
        time.sleep(0.1)
        if time.time() > timeout:
            break
    print('Last week option selected')
    elapsed2 = datetime.datetime.now()
    print("Elapsed Time2 = {0}".format(elapsed2 - start2))
    button5 = driver.find_element_by_xpath("//span[@class='filter-option pull-left']").click()
    button10 = driver.find_element_by_xpath("//span[contains(text(),'Last Month')]").click()
    start3 = datetime.datetime.now()
    timeout = time.time() + 60 * 2
    while len(driver.find_elements_by_css_selector("path[class='area areaChart']")) != 19:
        time.sleep(0.1)
        if time.time() > timeout:
            break

    print('Last month option selected')
    elapsed3 = datetime.datetime.now()
    end3 = (elapsed3 - start3).total_seconds()
    print("Elapsed Time3 = {0}".format(elapsed3 - start3))
    assert end3 <= 5, "Something has changed!"
    #driver.close()
function2()
function3()
function4()

