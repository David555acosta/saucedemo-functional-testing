from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest


#Verificar que sea posible agregar dos productos al carrito de compras.

#La automatización deberá:

#Agregar dos productos distintos.
#Acceder al carrito.
#Validar que ambos productos se encuentren presentes.
#Comparar los nombres obtenidos con los nombres esperados.

class casoDePrueba1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.quit()
    
    def test_buscar(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        productosAñadidos = []
        
        #Iniciar sesion
        nombre = driver.find_element(By.XPATH, "//*[@id='user-name']")
        contraseña = driver.find_element(By.XPATH, "//*[@id='password']")
        btnIngresar = driver.find_element(By.NAME, "login-button")
        
        time.sleep(3)
        
        nombre.send_keys("standard_user")
        contraseña.send_keys("secret_sauce")
        
        time.sleep(2)
        
        btnIngresar.click()
        
        time.sleep(5)
        
        articuloA = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
        nombreArticuloA = articuloA.text
        articuloA.click()
        
        time.sleep(2)
        
        btnAgregarArticulo = driver.find_element(By.NAME , "add-to-cart")
        btnAgregarArticulo.click()
        productosAñadidos.append(nombreArticuloA)
        
        time.sleep(2)
        
        btnVolverCatalogo = driver.find_element(By.NAME , "back-to-products")
        btnVolverCatalogo.click()
        
        
        time.sleep(2)
        
        articuloB = driver.find_element(By.XPATH, "//*[@id='item_3_title_link']")
        nombreArticuloB = articuloB.text
        articuloB.click()
        
        
        time.sleep(2)
        
        btnAgregarArticulo = driver.find_element(By.NAME , "add-to-cart")
        btnAgregarArticulo.click()
        productosAñadidos.append(nombreArticuloB)
        
        
        time.sleep(2)
        
        btnVolverCatalogo = driver.find_element(By.NAME , "back-to-products")
        btnVolverCatalogo.click()
        
        time.sleep(2)
        
        carrito = driver.find_element(By.XPATH , "//*[@id='shopping_cart_container']")
        carrito.click()
        
        time.sleep(5)
        
        items = driver.find_elements(By.XPATH, '//*[@data-test="inventory-item"]')

        nombres_carrito = []

        for item in items:
            nombre = item.find_element(By.XPATH, './/*[@data-test="inventory-item-name"]').text
            nombres_carrito.append(nombre)
            
        self.assertEqual(set(productosAñadidos), set(nombres_carrito))
        
        
        
if __name__ == '__main__':
    unittest.main()