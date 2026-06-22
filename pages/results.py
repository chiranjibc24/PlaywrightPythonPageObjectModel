
from playwright.sync_api import Page, expect

class resultsPage:
    def __init__(self, page: Page):
        self.page = page
        self.addToCartBtn = lambda product: page.locator(f"(//span[contains(text(),'{product}')]/ancestor::div[@data-component-type='s-search-result']//button[@aria-label='Add to cart'])[1]")
        self.cartCount = page.locator("#nav-cart-count")
        self.firstProduct = page.locator("[data-component-type='s-search-result']").first
        self.resultsHeading = page.get_by_text("Results", exact=True)
        self.sortDropdown = page.locator('[aria-label*="Sort by"]')
        self.sortButton = page.locator('button:has-text("Featured")')
        self.filterButton = page.locator('//div[@aria-label="filters"]')
        self.priceFilter = page.locator('[aria-label*="price"]')
        self.productContainer = page.locator('[data-component-type="s-search-result"]')

    def wait_for_results_loaded(self):
        self.productContainer.first.wait_for(state="visible", timeout=30000)

    def addAnItmeToCart(self, itemName):
        add_button = self.addToCartBtn(itemName)

        if not add_button.is_visible():
            self.firstProduct.click()
            self.page.wait_for_load_state("domcontentloaded")
            add_button = self.page.locator('input#add-to-cart-button, button#add-to-cart-button, button[name="submit.addToCart"]')

        add_button.wait_for(state="visible", timeout=30000)
        add_button.click()

    def wait_for_cart_count_change(self, previous_count: int):
        self.page.wait_for_function(
            "previous => Number(document.querySelector('#nav-cart-count')?.textContent.trim() || 0) > previous",
            arg=previous_count,
            timeout=60000,
        )

    def getCartCount(self):
        text = self.cartCount.text_content()
        return int(text.strip() or 0)
    

  