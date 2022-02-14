from selenium import webdriver               #cth use : drv.find_element_by_id("username").send_keys("idejongkok")
from selenium.webdriver.common.action_chains import ActionChains

#CARA INITIALIZE Start Page 3 DRIVER BROWSER YG SERING DIPAKAI | path sesuaikan ditempat driver .exe nya
#pilih salah 1 sesuai browser 
drv = webdriver.Firefox(executable_path=r'C:\webdriver\geckodriver.exe')
#drv = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe') 
#drv = webdriver.Ie(executable_path=r'C:\webdriver\IEDriverServer.exe')
#drv = webdriver.Chrome #kadang bs jg spt ini jika path nya ga direct otomatis

#CARA 1
drv.get("https://demoqa.com/menu")

