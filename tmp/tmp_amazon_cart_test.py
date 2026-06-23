from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.amazon.in/s?k=iphone+17', wait_until='domcontentloaded')
    page.wait_for_timeout(5000)
    sel = "(//span[contains(text(),'iPhone 17')]/ancestor::div[@data-component-type='s-search-result']//button[@aria-label='Add to cart'])[1]"
    btn = page.locator(sel)
    print('btn visible', btn.is_visible(), 'count', btn.count())
    if btn.is_visible():
        btn.click()
        page.wait_for_timeout(10000)
        print('after click url', page.url)
        print('after count', page.locator('#nav-cart-count').text_content())
        page.goto('https://www.amazon.in/gp/cart/view.html', wait_until='domcontentloaded')
        print('cart page url', page.url)
        print('cart page title', page.title())
        print('cart items count', page.locator('div.sc-list-item').count())
        if page.locator('div.sc-list-item').count() > 0:
            print('first cart item text:', page.locator('div.sc-list-item').first.text_content()[:200])
    browser.close()
