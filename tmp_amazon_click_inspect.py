from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.amazon.in/s?k=iphone+17', wait_until='domcontentloaded')
    sel = "(//span[contains(text(),'iPhone 17')]/ancestor::div[@data-component-type='s-search-result']//button[@aria-label='Add to cart'])[1]"
    btn = page.locator(sel)
    print('button visible', btn.is_visible(), 'count', btn.count())
    if btn.is_visible():
        btn.click()
        page.wait_for_timeout(5000)
        print('after click url', page.url)
        print('after cart count', page.locator('#nav-cart-count').text_content())
        for query in [
            'text=Added to Cart',
            'text=Added to Cart to Cart',
            'text=Added',
            'text=Added to',
            'text=added to cart',
            'text=Cart updated',
            '#attachDisplayAddBaseAlert',
            '#attach-sidesheet',
            '#attach-close_sideSheet-link',
            'div[id*="attach"]',
            'div[id*="added"]',
            'div[aria-label*="Added"], span[aria-label*="Added"], p:has-text("Added to Cart")',
        ]:
            try:
                locator = page.locator(query)
                print('query', query, 'count', locator.count(), 'visible', locator.is_visible() if locator.count() else 'n/a')
            except Exception as e:
                print('query error', query, e)
        print('page title:', page.title())
    browser.close()
