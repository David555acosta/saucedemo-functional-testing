from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        
        nombre = driver.find_element(By.XPATH, "//*[@id='user-name']")
        contraseña = driver.find_element(By.XPATH, "//*[@id='password']")
        btnIngresar = driver.find_element(By.NAME, "login-button")
        
        time.sleep(3)
        
        nombre.send_keys("standard_user")
        contraseña.send_keys("secret_sauce")
        
        time.sleep(2)
        
        btnIngresar.click()
        
        time.sleep(5)
        
        
        referenciaLoginExitoso = driver.find_element(By.XPATH, "//*[@id='header_container']")
        
        time.sleep(5)
        
        self.assertTrue(referenciaLoginExitoso.is_displayed())
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()