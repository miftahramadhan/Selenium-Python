from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

#pilih salah 1 sesuai browser
drv = webdriver.Firefox(executable_path=r'C:\webdriver\geckodriver.exe')
#drv = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe') 
#drv = webdriver.Ie(executable_path=r'C:\webdriver\IEDriverServer.exe')

drv.get('http://the-internet.herokuapp.com/windows')    #cth halaman saat diklik linknya membuka tab browser baru.
time.sleep(2)
drv.find_element_by_xpath('//*[@id="content"]/div/a').click()
time.sleep(2)
drv.switch_to.window(drv.window_handles[0]) # akan kembali ke tab awal.

time.sleep(2)
drv.find_element_by_xpath('//*[@id="content"]/div/a').click()
time.sleep(2)
drv.switch_to.window(drv.window_handles[0])
time.sleep(2)
drv.find_element_by_xpath('//*[@id="content"]/div/a').click()
time.sleep(2)
drv.switch_to.window(drv.window_handles[0])

