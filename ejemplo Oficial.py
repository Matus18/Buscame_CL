from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import time

path = r"C:\Users\benja\Downloads\chromedriver"
driver = webdriver.Chrome(path)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.pjud.cl/')


def pjud():
    login_1 = driver.find_element(By.XPATH, "//a[@href='https://oficinajudicialvirtual.pjud.cl/includes/sesion-consultaunificada.php'][1]") 
    login_1.click()
    time.sleep(1)

#ENCONTRAR ERROR EN EL HTML DE LA PAGINA 'https://oficinajudicialvirtual.pjud.cl/indexN.php' 

def busqueda_por_nombre():
    nombre = input("Ingresar Nombre: ")
    apellido_paterno = input("Ingresar Apellido Paterno: ")
    apellido_materno = input("Ingresar Apellido Materno: ")
    
    nombre = driver.find_element(By.ID, "'nomNombre'") #ID
    nombre.send_keys(nombre)
    
    apellido_paterno = driver.find_element(By.ID, "nomApePaterno") #
    apellido_paterno.send_keys(Keys.RETURN, apellido_paterno)
    
    apellido_materno = driver.find_element(By. ID, "nomApeMaterno") 
    apellido_materno.send_keys(Keys.RETURN, apellido_materno)

def tabla_caratulado():
    r = requests.get('https://oficinajudicialvirtual.pjud.cl/indexN.php')
    soup = BeautifulSoup(r.text, 'html.parser')
    
    tabla_caratulado = soup.find('table', class_='table table-bordered table-striped table-hover')
    
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
    

driver.quit()
