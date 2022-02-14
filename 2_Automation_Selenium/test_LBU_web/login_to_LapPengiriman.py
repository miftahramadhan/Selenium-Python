from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC, select, wait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep as delay

#drv = webdriver.Ie(executable_path=r'C:\webdriver\IEDriverServer.exe')
drv = webdriver.Firefox(executable_path=r'C:\webdriver\geckodriver.exe')
drv.get("http://localhost:3535/Default.aspx")
drv.find_element(By.CLASS_NAME, 'field').send_keys("miftah_r")
delay(1)
drv.find_element(By.ID, 'ctl00_MainContent_txtPassword').send_keys('ws123456!')
delay(1)
drv.find_element(By.ID, 'ctl00_MainContent_btnLogin').click()
ActionChains(drv).move_to_element(drv.find_element_by_link_text("Laporan")).perform()
delay(1)
drv.find_element_by_link_text("Laporan Pengiriman").click()

#comboBOX :
periode = Select (drv.find_element_by_id('ctl00_MainContent_DefaultContent_ctrlFilter_drdPeriode'))
delay(2)
periode.select_by_visible_text("12 - 2021")
drv.find_element_by_id("ctl00_MainContent_DefaultContent_ctrlFilter_btnTampil").click()


#drv.find_element(By.CLASS_NAME, 'ctl00_MainMenuContent_MainMenu_1 ctl00_MainMenuContent_MainMenu_5 ctl00_MainMenuContent_MainMenu_14').click()


#cara / inssight lain
#txtuser = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'field')))
#txtuser.send_keys("miftah")
#txtuser.send_keys(Keys.ENTER)
