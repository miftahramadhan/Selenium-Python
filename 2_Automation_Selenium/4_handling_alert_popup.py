from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

#pilih salah 1 sesuai browser
#drv = webdriver.Firefox(executable_path=r'C:\webdriver\geckodriver.exe')
drv = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe') 
#drv = webdriver.Ie(executable_path=r'C:\webdriver\IEDriverServer.exe')

drv.get('https://demoqa.com/alerts')    #cth halaman untuk case popup/alert notif
time.sleep(1)
drv.maximize_window()
time.sleep(1)

drv.find_element_by_id('alertButton').click() #<<<---- Button menghasilkan 1 pilihan alert (ok)
#drv.find_element_by_id('confirmButton').click() #<<<---- Button menghasilkan 2 pilihan alert (ok atau cancel)
#drv.find_element_by_id('promtButton').click() #<<<---- Button menghasilkan isian textbox yg hrs diisi
time.sleep(3)

drv.switch_to.alert.accept()                   # <<<-----fungsi handling alert 1 pilihan : OK(Accept)
#drv.switch_to.alert.dismiss()                   # <<<-----fungsi handling alert 2 pilihan (ok/Cancel) : memilih cancel(Dismiss)
#drv.switch_to.alert.send_keys('saya sedang test')  # <<<-----fungsi handling alert mengisi textboxt alert 

time.sleep(2)
drv.find_element_by_class_name('header-wrapper').click()
time.sleep(1)
drv.find_element_by_class_name('text').click()
time.sleep(2)
drv.find_element_by_css_selector('#userName').send_keys('Miftah Kerensss')

### IE ##
"""
import os
iedriver = "C:\ie\IEDriverServer.exe"
os.environ["webdriver.ie.driver"]= iedriver
drv = webdriver.Ie(iedriver)
drv.get('http://lbubasel.corp.bi.go.id/lbubasel')
drv.find_element_by_id("ctl00_MainContent_txtUserName").send_keys("miftah")
time.sleep(2)
drv.find_element_by_id("ctl00_MainContent_txtPassword").send_keys("ws123456!")
time.sleep(2)
"""


