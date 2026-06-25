from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest


#Luego de agregar los productos indicados en el Caso de Prueba 2, validar que la cantidad de productos presentes
#en el carrito coincida con la cantidad esperada.

#La automatización deberá obtener la cantidad real de productos mostrados en el carrito y compararla con la cantidad esperada.

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
        
        time.sleep(5)
        
        nombre.send_keys("standard_user")
        contraseña.send_keys("secret_sauce")
        
        time.sleep(5)
        
        btnIngresar.click()
        
        time.sleep(5)
        
        articuloA = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
        nombreArticuloA = articuloA.text
        articuloA.click()
        
        time.sleep(5)
        
        btnAgregarArticulo = driver.find_element(By.NAME , "add-to-cart")
        btnAgregarArticulo.click()
        productosAñadidos.append(nombreArticuloA)
        
        time.sleep(5)
        
        btnVolverCatalogo = driver.find_element(By.NAME , "back-to-products")
        btnVolverCatalogo.click()
        
        
        time.sleep(5)
        
        articuloB = driver.find_element(By.XPATH, "//*[@id='item_3_title_link']")
        nombreArticuloB = articuloB.text
        articuloB.click()
        
        
        time.sleep(5)
        
        btnAgregarArticulo = driver.find_element(By.NAME , "add-to-cart")
        btnAgregarArticulo.click()
        productosAñadidos.append(nombreArticuloB)
        
        
        time.sleep(5)
        
        btnVolverCatalogo = driver.find_element(By.NAME , "back-to-products")
        btnVolverCatalogo.click()
        
        time.sleep(5)
        
        carrito = driver.find_element(By.XPATH , "//*[@id='shopping_cart_container']")
        carrito.click()
        
        time.sleep(5)
        
        items = driver.find_elements(By.XPATH, '//*[@data-test="inventory-item"]')

        nombres_carrito = []

        for item in items:
            nombre = item.find_element(By.XPATH, './/*[@data-test="inventory-item-name"]').text
            nombres_carrito.append(nombre)
            
            
        cantidadEsperada = len(productosAñadidos)
        
        cantidadElementosEnCarrito = driver.find_element(By.CLASS_NAME , "shopping_cart_badge")
        cantidadElementosEnCarritoContent = int(cantidadElementosEnCarrito.text)
        
        self.assertEqual(cantidadEsperada, cantidadElementosEnCarritoContent)
        self.assertEqual(set(productosAñadidos), set(nombres_carrito))
        
        
        
if __name__ == '__main__':
    unittest.main()