from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.reader import read_products_json

def test_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    
    driver.get("https://saucedemo.com/")

    login_page.login("standard_user","secret_sauce")

    # Leer el 1er prod del Json
    producto = read_products_json()[0]
    print(producto)

     # Agregar prod del Json
    inventory_page.agregar_producto(producto["nombre"])

    assert inventory_page.obtener_contador_carrito() == "1"

    # Ir al carrito
    inventory_page.ir_al_carrito()

    # Validar nombre contra el Json
    assert cart_page.obtener_nombreproducto() == producto["nombre"]

    # Validar precio contra el Json
    assert cart_page.obtener_precio_producto() == producto["precio"]