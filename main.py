from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/Popuś/Desktop/Python/environment_variables/.env")
LINKED_IN_USERNAME = os.getenv("linkedin_username")
LINKED_IN_PASSWORD = os.getenv("linkedin_password")
MY_PHONE = int(os.getenv("my_phone"))


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_drive_path = r" C:\Selenium\chrome_driver.exe "
ser = Service(chrome_drive_path)
driver = webdriver.Chrome(service=ser, options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3585688852&f_AL=true&f_E=1%2C2&f_T=25169%2C25194%2C25201&f_TPR=r2592000&geoId=105072130&keywords=JUNIOR%20python%20developer&location=Polska&refresh=true&sortBy=DD")


####CLICK APPLY BUTTON ON FIRST JOB############################################################
login_button = driver.find_element(By.LINK_TEXT, "Zaloguj się")
login_button.click()

# Wait for laoding new page
time.sleep(3)

####LOGIN FORM PAGE############################################################
username_field = driver.find_element(By.ID, "username")
username_field.send_keys(LINKED_IN_USERNAME)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(LINKED_IN_PASSWORD)

password_field.send_keys(Keys.ENTER)

# Wait for laoding new page
time.sleep(3)

easy_apply_button = driver.find_element(By.CLASS_NAME,"jobs-apply-button")
easy_apply_button.click()

# Wait for laoding new page
time.sleep(3)

####CONTACT DETAILS PAGE############################################################


phone_nr_input = driver.find_element(By.ID,"single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3585688852-87472227-phoneNumber-nationalNumber")
# phone_nr_input.send_keys(f"{MY_PHONE}")

#fill input only when is not pre-poluated
if phone_nr_input.text =="":
    phone_nr_input.send_keys(f"{MY_PHONE}")

next_button = driver.find_element(By.ID,"ember485")
next_button.click()

# Wait for laoding new page
time.sleep(3)

####RESUME PAGE########################################################################
next_button_2 = driver.find_element(By.ID,"ember485")
next_button_2.click()

# Wait for laoding new page
time.sleep(3)

##QUESTIONS PAGE#####################################################################
experience_input = driver.find_element(By.ID,"single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3585688852-87472483-numeric")
experience_input.send_keys("1")


#Dropdown select
location_select = Select(driver.find_element(By.ID, "text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3585688852-87472475-multipleChoice"))
location_select.select_by_index(1)


# Wait for laoding new page
time.sleep(3)

next_button_3 = driver.find_element(By.ID,"ember491")
next_button_3.click()


##FINAL PAGE#####################################################################

follow_company_checkbox = driver.find_element(By.CLASS_NAME,"job-details-easy-apply-footer__section")
follow_company_checkbox.click()



# submit_button = driver.find_element(By.ID,"ember546")
# submit_button.click()


# # ------- english proficiency drop down--------
# drop_box = driver.find_element(By.ID, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2914739616,43805589,multipleChoice)')
# # select drop down menu
# english_drop = Select(drop_box)
# # select option from drop down menu (using select by index) it's our own choice
# english_drop.select_by_index(2)


# # --------work experience drop down--------
# next_drop_box = driver.find_element(By.ID, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized'
#                                            '_jobPosting:2914739616,43805581,multipleChoice)')

# experience_box = Select(next_drop_box)
# # select option from drop down menu (using select by Visible text) it's our own choice
# experience_box.select_by_visible_text('Yes')
# click_review = driver.find_element(By.CSS_SELECTOR, '.justify-flex-end .artdeco-button--primary').click()

# # click on submit------Your application will be submitted
# click_submit = driver.find_element(By.CSS_SELECTOR, '.justify-flex-end .artdeco-button--primary').click()
