from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def ingresar_usuario(self, usuario):
        self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys(usuario)
        logger.info("Usuario ingresado")

    def ingresar_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
        logger.info("Contraseña ingresada")

    def hacer_click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
        logger.info("Click en el botón de login")

    def obtener_mensaje_error(self):
        texto_error = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".error > h3"))
        )
        logger.info("Mensaje de error obtenido")
        return texto_error.text

    def login(self, usuario, password):
        logger.info("Iniciando proceso de login")
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.hacer_click_login()
        logger.info("Proceso de login ejecutado")
