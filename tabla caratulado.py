from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

path = r"C:\Users\benja\Downloads\chromedriver"
driver = webdriver.Chrome(path)

driver.get =('https://oficinajudicialvirtual.pjud.cl/indexN.php')
r = requests.get('https://oficinajudicialvirtual.pjud.cl/indexN.php')
soup = BeautifulSoup(r.text, 'html.parser')

tabla_caratulado = soup.find('table', class_='table table-bordered table-striped table-hover')

#INFORMACION DE LA TABLA
rol = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[2]/div[1]/div/section/div[1]/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[1]/td[2]')
rol.get_attribute()

tipo_recurso = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[2]/div[1]/div/section/div[1]/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[1]/td[3]')
tipo_recurso.get_attribute()

caratulado = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[2]/div[1]/div/section/div[1]/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[1]/td[4]')
caratulado.get_attribute()

fecha_ingreso = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[2]/div[1]/div/section/div[1]/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[1]/td[5]')
fecha_ingreso.get_attribute()

estado_causa = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[2]/div[1]/div/section/div[1]/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[1]/td[6]')
estado_causa.get_attribute()

corte = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[2]/div[1]/div/section/div[1]/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[1]/td[7]')
corte.get_attribute()

lupa = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[2]/div[1]/div/section/div[1]/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[1]/td[1]')
lupa.click()


