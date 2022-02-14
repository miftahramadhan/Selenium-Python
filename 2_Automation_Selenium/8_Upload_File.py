from selenium import webdriver
import pyautogui                        #utk cara 2
import time

drv = webdriver.Chrome()
drv.implicitly_wait(120)
drv.maximize_window()
time.sleep(2)

#ALAMAT Untuk cara 1
#drv.get("https://demoqa.com/upload-download")

#ALAMAT Untuk cara 2
drv.get("https://gofile.io/uploadFiles")
time.sleep(3)
#CARA 1:
#drv.find_element_by_id('uploadFile').send_keys('C:/Users/miftah/Downloads/Tugas_19.pdf')

#CARA 2:
drv.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[13]/div/div/div/div/div/div[1]/div/button').click()
time.sleep(3)
pyautogui.write(r"C:\Users\miftah\Downloads\Tugas_19.pdf")
pyautogui.press("enter")