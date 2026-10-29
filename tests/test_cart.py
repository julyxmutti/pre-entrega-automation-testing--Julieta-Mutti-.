
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.reader import read_products_json
from utils.logger import logger

def test_cart(driver):
    try:
        logger.info("Iniciando prueba del carrito")

        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        driver.get("https://saucedemo.com/")
        logger.info("Pagina abierta correctamente")

        login_page.login("standard_user", "secret_sauce")
        logger.info("Ingreso de credenciales")

        # Leer el 1er producto del JSON
        producto = read_products_json()[0]
        logger.info("Producto obtenido del JSON")

        # Agregar producto del JSON
        inventory_page.agregar_producto(producto["nombre"])
        logger.info("Producto agregado al carrito")

        assert inventory_page.obtener_contador_carrito() == "1"
        logger.info("Contador del carrito validado")

        # Ir al carrito
        inventory_page.ir_al_carrito()
        logger.info("Ingreso al carrito")

        # Validar nombre contra el JSON
        assert cart_page.obtener_nombreproducto() == producto["nombre"]
        logger.info("Nombre del producto validado")

        # Validar precio contra el JSON
        assert cart_page.obtener_precio_producto() == producto["precio"]
        logger.info("Precio del producto validado")

    except Exception:
        logger.exception("Error durante la prueba del carrito")
        raise
