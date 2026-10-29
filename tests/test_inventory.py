
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

def test_inventory(driver):
    try:
        logger.info("Iniciando prueba de inventario")

        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        driver.get("https://www.saucedemo.com/")
        logger.info("Pagina abierta correctamente")

        login_page.login("standard_user", "secret_sauce")
        logger.info("Ingreso de credenciales")

        productos = inventory_page.obtener_productos()
        logger.info("Productos obtenidos correctamente")

        assert len(productos) > 0
        logger.info("Se verifico que existan productos")

        assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
        logger.info("Nombre del primer producto validado")

        assert inventory_page.obtener_precio_primer_producto() == "$29.99"
        logger.info("Precio del primer producto validado")

        assert inventory_page.menu_visible()
        logger.info("Menu visible")

        assert inventory_page.filtro_visible()
        logger.info("Filtro visible")

    except Exception:
        logger.exception("Error durante la prueba de inventario")
        raise
