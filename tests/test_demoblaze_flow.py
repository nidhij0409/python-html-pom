from lib import *
from pages.demoblaze_page import DemoblazePage

def test_demoblaze_monitor_purchase_flow(get_driver):
    driver = get_driver
    page = DemoblazePage(driver)

    page.open_site()
    page.go_to_monitors()
    page.open_asus_fullhd()
    page.add_to_cart_and_confirm()
    page.go_to_cart()

    cart_product = page.validate_product_in_cart()
    print("Product in cart:", cart_product)

    page.click_place_order()
    print("Place order modal opened successfully.")

    page.fill_place_order_form()
    print("Order placed successfully.")
