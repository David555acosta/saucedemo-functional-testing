from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


#Verificar que, al ingresar credenciales válidas, el usuario acceda correctamente al sistema y visualice la pantalla de
# productos. La automatización deberá
# validar que el login fue exitoso mediante algún elemento visible de la pantalla posterior al acceso. 

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