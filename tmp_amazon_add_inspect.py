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
        print('added confirmation count', page.locator('text=Added to Cart').count())
        print('add-to-cart alert count', page.locator('#attachDisplayAddBaseAlert').count())
        print('attach close count', page.locator('#attach-close_sideSheet-link').count())
        print('page content snippet', page.content()[:1000])
    browser.close()
