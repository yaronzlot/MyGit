# ***** BuyMe sanity text *****

# Pre-Requisites:
    # pip install Pillow
    # pip install pynput
    # chromedriver.exe should be located in c:\\temp

import time
from pynput.keyboard import Key, Controller
from PIL import Image, ImageDraw
from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:/temp/chromedriver.exe")

try:
    # Step A - registration screen
    # Enter the web site
    driver.get("https://buyme.co.il")
    driver.maximize_window()
    time.sleep(5)
    # Press button enter|registration
    driver.find_element_by_xpath("//li[@class='top-bar-item my-account']").click()
    # Press button "not yet registration"
    driver.find_element_by_xpath("/html/body[@class='ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember542']/div[@class='main-container main-padding']/div[@id='ember889']/div[@id='auth-modal']/div[@class='modal modal--auth modal--extra-wide']/span[@class='header-link bold']/strong").click()
    # enter first name
    driver.find_element_by_xpath("/html/body[@class='ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember542']/div[@class='main-container main-padding']/div[@id='ember889']/div[@id='auth-modal']/div[@class='modal modal--auth modal--extra-wide']/div[@class='row row--md relative']/div[@class='col col-1-2'][2]/div[@class='auth-modal-wrapper']/div[@id='register-block']/form[@id='ember900']/div[@class='form-group'][1]/div[@class='input-with-icon-wrapper relative']/input[@id='ember901']").send_keys("yaron")
    # enter email address
    driver.find_element_by_xpath("//html/body[@class='ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember542']/div[@class='main-container main-padding']/div[@id='ember889']/div[@id='auth-modal']/div[@class='modal modal--auth modal--extra-wide']/div[@class='row row--md relative']/div[@class='col col-1-2'][2]/div[@class='auth-modal-wrapper']/div[@id='register-block']/form[@id='ember900']/div[@class='form-group'][2]/div[@class='input-with-icon-wrapper relative']/input[@id='ember902']").send_keys("yaron.zlotolov@gmail.com")
    # enter password
    driver.find_element_by_xpath("/html/body[@class='ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember542']/div[@class='main-container main-padding']/div[@id='ember889']/div[@id='auth-modal']/div[@class='modal modal--auth modal--extra-wide']/div[@class='row row--md relative']/div[@class='col col-1-2'][2]/div[@class='auth-modal-wrapper']/div[@id='register-block']/form[@id='ember900']/div[@class='form-group'][3]/div[@class='input-with-icon-wrapper relative']/input[@id='valPass']").send_keys("1qaz!QAZ")
    # enter password again
    driver.find_element_by_xpath("/html/body[@class='ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember542']/div[@class='main-container main-padding']/div[@id='ember889']/div[@id='auth-modal']/div[@class='modal modal--auth modal--extra-wide']/div[@class='row row--md relative']/div[@class='col col-1-2'][2]/div[@class='auth-modal-wrapper']/div[@id='register-block']/form[@id='ember900']/div[@class='form-group'][4]/div[@class='input-with-icon-wrapper relative']/input[@id='ember904']").send_keys("1qaz!QAZ")
    # press on radion button "I agree"
    driver.find_element_by_xpath("/html/body[@class='ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember542']/div[@class='main-container main-padding']/div[@id='ember889']/div[@id='auth-modal']/div[@class='modal modal--auth modal--extra-wide']/div[@class='row row--md relative']/div[@class='col col-1-2'][2]/div[@class='auth-modal-wrapper']/div[@id='register-block']/form[@id='ember900']/div[@class='form-group'][5]/div/label").click()
    # press button "registration"
    driver.find_element_by_xpath("/html/body[@class='ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember542']/div[@class='main-container main-padding']/div[@id='ember889']/div[@id='auth-modal']/div[@class='modal modal--auth modal--extra-wide']/div[@class='row row--md relative']/div[@class='col col-1-2'][2]/div[@class='auth-modal-wrapper']/div[@id='register-block']/form[@id='ember900']/button[@class='db fluid btn btn-theme']").click()
    time.sleep(5)
except:
    # in case the user already registered
    driver.quit()
finally:
    # Step B - home screen
    # log in
    driver.get("https://buyme.co.il")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element_by_xpath("//li[@class='top-bar-item my-account']").click()
    # enter first name
    driver.find_element_by_xpath("/html/body[@class='ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember542']/div[@class='main-container main-padding']/div[@id='ember889']/div[@id='auth-modal']/div[@class='modal modal--auth modal--extra-wide']/div[@class='row row--md relative']/div[@class='col col-1-2'][2]/div[@class='auth-modal-wrapper']/div[@id='login-block']/form[@id='ember894']/div[@class='form-group'][1]/div[@class='input-with-icon-wrapper']/input[@id='ember895']").send_keys("yaron.zlotolov@gmail.com")
    # enter email address
    driver.find_element_by_xpath("/html/body[@class='ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember542']/div[@class='main-container main-padding']/div[@id='ember889']/div[@id='auth-modal']/div[@class='modal modal--auth modal--extra-wide']/div[@class='row row--md relative']/div[@class='col col-1-2'][2]/div[@class='auth-modal-wrapper']/div[@id='login-block']/form[@id='ember894']/div[@class='form-group'][2]/div[@class='input-with-icon-wrapper']/input[@id='ember896']").send_keys("1qaz!QAZ")
    # remember me
    driver.find_element_by_xpath("/html/body[@class='ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember542']/div[@class='main-container main-padding']/div[@id='ember889']/div[@id='auth-modal']/div[@class='modal modal--auth modal--extra-wide']/div[@class='row row--md relative']/div[@class='col col-1-2'][2]/div[@class='auth-modal-wrapper']/div[@id='login-block']/form[@id='ember894']/footer[@class='clearfix']/div[@class='check-wrapper']/label").click()
    # click enter
    driver.find_element_by_xpath("/html/body[@class='ember-application INDpositionRight INDDesktop INDChrome INDlangdirRTL hover']/div[@id='ember542']/div[@class='main-container main-padding']/div[@id='ember889']/div[@id='auth-modal']/div[@class='modal modal--auth modal--extra-wide']/div[@class='row row--md relative']/div[@class='col col-1-2'][2]/div[@class='auth-modal-wrapper']/div[@id='login-block']/form[@id='ember894']/button[@class='db fluid btn btn-theme']").click()
    time.sleep(5)
    # pick a price point
    dropbox = driver.find_elements_by_class_name("chosen-container")
    dropbox[0].click()
    result = driver.find_elements_by_class_name("active-result")
    result[2].click()
    # pick the area
    dropbox = driver.find_elements_by_class_name("chosen-container")
    dropbox[1].click()
    result = driver.find_elements_by_class_name("active-result")
    result[2].click()
    # pick category
    dropbox = driver.find_elements_by_class_name("chosen-container")
    dropbox[2].click()
    result = driver.find_elements_by_class_name("active-result")
    result[2].click()
    # press the search button
    driver.find_element_by_class_name("btn-primary").click()

    # Step C - choose business screen
    # pick a business
    time.sleep(3)
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(3)
    driver.find_element_by_xpath("//div[@class='col col-1-3 col-sm-1-2'][2]").click()
    time.sleep(3)
    # type a price
    driver.find_element_by_class_name("input-cash").send_keys("150")
    time.sleep(3)
    btn = driver.find_elements_by_xpath("//button[@class='btn btn-theme']")
    # for ii in btn:
    #     print(ii.get_attribute('class'))
    btn[1].click()
    # Step D - sender & receiver information screen
    # press radio button "for someone else"
    time.sleep(3)
    driver.find_element_by_xpath("//label[@class='selected']").click()
    # enter receiver name
    rcv_name = driver.find_elements_by_class_name("ember-text-field")
    # for ii in rcv_name:
    #     print(ii.get_attribute('class'))
    rcv_name[2].clear()
    rcv_name[2].send_keys("איילת")
    # enter sender name
    rcv_name[3].clear()
    rcv_name[3].send_keys("ירון שי עמית ואיתי")
    # enter a blessing
    driver.find_element_by_xpath("//textarea").clear()
    driver.find_element_by_xpath("//textarea").send_keys("מזל טוב איילת!")
    rcv_name[4].click()
    # Upload a picture
    # pip install Pillow
    # creating an image for the test
    img = Image.new('RGB', (120, 50), color='red')
    d = ImageDraw.Draw(img)
    d.text((30, 20), "Mazal Tov", fill=(255, 255, 0))
    img.save('c:/temp/mazaltov.jpg')
    # pip install pynput - for uploading the picture from the local drive using the the keyboard
    time.sleep(3)
    keyboard = Controller()
    keyboard.type("c:\\temp\\mazaltov.jpg")
    keyboard.press(Key.enter)
    # pick the event - birthday
    time.sleep(3)
    events = driver.find_elements_by_class_name("chosen-container-single-nosearch")
    # for ii in events:
    #     print(ii.get_attribute('class'))
    events[4].click()
    result = driver.find_elements_by_class_name("active-result")
    result[1].click()
    # press radio button 'right after payment'
    driver.find_element_by_class_name("send-now").click()
    # pick email/sms option - sms
    driver.find_element_by_xpath("//span[@class='icon icon-sms']").click()
    # enter sender phone number
    phone = driver.find_elements_by_class_name("ember-text-field")
    # for ii in phone:
    #     print(ii.get_attribute('class'))
    phone[5].clear()
    phone[5].send_keys("052-3776494")
    # enter receiver phone number
    driver.find_element_by_xpath("//input[@id='resendReciver']").clear()
    driver.find_element_by_xpath("//input[@id='resendReciver']").send_keys("052-2475588")
    # press the save button
    driver.find_element_by_class_name("btn-save").click()
    # press submit
    submit = driver.find_elements_by_class_name("btn-theme")
    submit[2].click()



