from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.amazon.in', wait_until='domcontentloaded')
    print('home url', page.url)
    page.goto('https://www.amazon.in/s?k=iphone+17', wait_until='domcontentloaded')
    print('search url', page.url)
    print('nav count exists', page.locator('#nav-cart-count').count())
    print('nav count text', page.locator('#nav-cart-count').text_content())
    print('result count', page.locator('[data-component-type="s-search-result"]').count())
    sel = "(//span[contains(text(),'iPhone 17')]/ancestor::div[@data-component-type='s-search-result']//button[@aria-label='Add to cart'])[1]"
    print('iPhone 17 add button count', page.locator(sel).count())
    browser.close()
