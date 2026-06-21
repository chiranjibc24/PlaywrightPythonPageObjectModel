
from playwright.sync_api import Page, expect

class resultsPage:
    def __init__(self, page: Page):
        self.page = page
        # self.addToCartBtn = page.locator("(//span[contains(text(),'iPhone 16 Pro 256 GB')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@aria-label='Add to cart'])[1]")
        self.addToCartBtn = lambda product: page.locator(f"(//span[contains(text(),'{product}')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@aria-label='Add to cart'])[1]")
        #def addToCartBtn(self, product):
        #     return page.locator(f"(//span[contains(text(),'{product}')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//button[@aria-label='Add to cart'])[1]")
        self.cartCount = page.locator("#nav-cart-count")
        self.firstProduct = page.locator("#a-autoid-3-announce")
        self.resultsHeading = page.get_by_text("Results", exact=True)
        self.sortDropdown = page.locator('[aria-label*="Sort by"]')
        self.sortButton = page.locator('button:has-text("Featured")')
        self.filterButton = page.locator('//div[@aria-label="filters"]')
        self.priceFilter = page.locator('[aria-label*="price"]')
        self.productContainer = page.locator('[data-component-type="s-search-result"]')

    
    def addAnItmeToCart(self, itemName):
        self.addToCartBtn(itemName).click()

    
    def getCartCount(self):
        return self.cartCount.text_content()
    

  