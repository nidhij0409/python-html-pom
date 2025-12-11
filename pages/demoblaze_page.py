# pages/demoblaze_page.py
import lib

class DemoblazePage:
    url = "https://www.demoblaze.com/"

    # locators (prioritized / robust)
    categories_monitors = "//a[normalize-space()='Monitors']"
    product_asus_fullhd = "//a[contains(normalize-space(),'ASUS') and contains(normalize-space(),'Full')]"   # primary
    product_asus = "//a[contains(normalize-space(),'ASUS')]"                                              # fallback
    product_cards_container = "//div[@id='tbodyid']"                                                      # product listing / details container
    product_title_on_productpage = "//div[@id='tbodyid']//h2 | //h2"                                      # title on product page
    add_to_cart_btn = "//a[normalize-space()='Add to cart']"
    # alert text on add → "Product added."
    cart_link = "//a[@id='cartur' or normalize-space()='Cart']"
    cart_table_rows = "//tbody[@id='tbodyid']"
    cart_first_product_name = "(//tbody[@id='tbodyid']//tr/td[2])[1]"
    place_order_btn = "//button[normalize-space()='Place Order']"
    modal_ok_button = "//button[normalize-space()='OK']"   # generic fallback if site uses modal OK
    # user details to place order
    place_order_modal = "//div[@class='modal-content'][1]"
    name_field = "//input[@id='name']"
    country_field = "//input[@id='country']"
    city_field = "//input[@id='city']"
    card_field = "//input[@id='card']"
    month_field = "//input[@id='month']"
    year_field = "//input[@id='year']"
    purchase_btn = "//button[normalize-space()='Purchase']"

    def __init__(self, driver=None):

        self.driver = driver or lib.get_driver() or lib.create_driver()
        self.selected_product_name = None

    def open_site(self):
        self.driver.get(self.url)
        lib.time.sleep(3)   # allow page to load (site is JS heavy)

    def go_to_monitors(self):
        cat = lib.WebDriverWait(self.driver, 8).until(
            lib.EC.element_to_be_clickable((lib.By.XPATH, self.categories_monitors))
        )
        cat.click()
        # wait for product list to refresh
        lib.WebDriverWait(self.driver, 8).until(
            lib.EC.presence_of_element_located((lib.By.XPATH, self.product_cards_container))
        )
        lib.time.sleep(1)

    def open_asus_fullhd(self):
        # try primary locator first, then fallback
        try:
            prod = lib.WebDriverWait(self.driver, 6).until(
                lib.EC.element_to_be_clickable((lib.By.XPATH, self.product_asus_fullhd))
            )
        except Exception:
            prod = lib.WebDriverWait(self.driver, 6).until(
                lib.EC.element_to_be_clickable((lib.By.XPATH, self.product_asus))
            )
        # save link text (partial) before click if possible
        try:
            self.selected_product_name = prod.text.strip()
        except Exception:
            self.selected_product_name = None
        prod.click()

        # wait for product page to load and capture exact title
        title_el = lib.WebDriverWait(self.driver, 8).until(
            lib.EC.visibility_of_element_located((lib.By.XPATH, self.product_title_on_productpage))
        )
        # finalize saved product name (exact title)
        self.selected_product_name = title_el.text.strip()

    def add_to_cart_and_confirm(self):
        # click Add to cart
        add_btn = lib.WebDriverWait(self.driver, 8).until(
            lib.EC.element_to_be_clickable((lib.By.XPATH, self.add_to_cart_btn))
        )
        add_btn.click()

        # wait for alert and validate text
        try:
            alert = lib.WebDriverWait(self.driver, 10).until(lib.EC.alert_is_present())
            alert_text = alert.text
            assert "Product added" in alert_text, f"Unexpected alert text: {alert_text}"
            alert.accept()
            lib.time.sleep(1)
        except Exception:
            raise AssertionError("JS alert not appearing after Add to cart.")

    def go_to_cart(self):
        cart = lib.WebDriverWait(self.driver, 8).until(
            lib.EC.element_to_be_clickable((lib.By.XPATH, self.cart_link))
        )
        cart.click()
        # wait for cart rows to load
        lib.WebDriverWait(self.driver, 15).until(
            lib.EC.presence_of_element_located((lib.By.XPATH, self.cart_table_rows))
        )
        lib.time.sleep(5)

    def validate_product_in_cart(self):
        # get first product name in cart
        try:
            name_el = lib.WebDriverWait(self.driver, 6).until(
                lib.EC.visibility_of_element_located((lib.By.XPATH, self.cart_first_product_name))
            )
            cart_name = name_el.text.strip()
        except Exception:
            raise AssertionError("No product found in cart to validate.")

        # if we saved selected_product_name earlier, compare
        if self.selected_product_name:
            assert self.selected_product_name in cart_name or cart_name in self.selected_product_name, \
                f"Cart product name mismatch. Expected: {self.selected_product_name!r}, Found: {cart_name!r}"
        return cart_name

    def click_place_order(self):
        btn = lib.WebDriverWait(self.driver, 8).until(
            lib.EC.element_to_be_clickable((lib.By.XPATH, self.place_order_btn))
        )
        btn.click()
        # wait briefly for order modal / page
        lib.time.sleep(1)

    def fill_place_order_form(self):
        # # wait for modal
        # lib.WebDriverWait(self.driver, 10).until(
        #     lib.EC.visibility_of_element_located((lib.By.XPATH, self.place_order_modal))
        # )

        # enter values
        self.driver.find_element(lib.By.XPATH, self.name_field).send_keys("Nidhi")
        self.driver.find_element(lib.By.XPATH, self.country_field).send_keys("India")
        self.driver.find_element(lib.By.XPATH, self.city_field).send_keys("Ahmedabad")
        self.driver.find_element(lib.By.XPATH, self.card_field).send_keys("4111111111111111")
        self.driver.find_element(lib.By.XPATH, self.month_field).send_keys("12")
        self.driver.find_element(lib.By.XPATH, self.year_field).send_keys("2025")

        # click Purchase
        self.driver.find_element(lib.By.XPATH, self.purchase_btn).click()

        lib.time.sleep(1)

