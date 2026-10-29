
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_nombreproducto(self):
        nombre = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        ).text
        logger.info("Nombre del producto obtenido del carrito")
        return nombre

    def obtener_precio_producto(self):
        precio = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_price")
            )
        ).text
        logger.info("Precio del producto obtenido del carrito")
        return float(precio.replace("$", ""))
