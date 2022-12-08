from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

path = r"C:\Users\benja\Downloads\chromedriver"
driver = webdriver.Chrome(path)

#PAGINA PRINCIPAL "WWW.PJUD.CL"
driver.get('https://www.pjud.cl/')

#INGRESO A OFICINA JUDICIAL VIRTUAL
link = driver.find_element(By.XPATH, "//a[@href='https://oficinajudicialvirtual.pjud.cl/includes/sesion-consultaunificada.php'][1]")
link.click()
time.sleep(1)

