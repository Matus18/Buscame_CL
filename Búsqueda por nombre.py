from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

path = r"C:\Users\benja\Downloads\chromedriver"
driver = webdriver.Chrome(path)

def busqueda_por_nombre():
    nombre = input("Ingresar Nombre: ")
    apellido_paterno = input("Ingresar Apellido Paterno: ")
    apellido_materno = input("Ingresar Apellido Materno: ")
    
    nombre = driver.find_element(By.ID, "'nomNombre'") #ID
    nombre.send_keys(nombre)
    
    apellido_paterno = driver.find_element(By.ID, "nomApePaterno") #ID
    apellido_paterno.send_keys(Keys.RETURN, apellido_paterno)
    
    apellido_materno = driver.find_element(By. ID, "nomApeMaterno") #ID
    apellido_materno.send_keys(Keys.RETURN, apellido_materno)

driver.quit()