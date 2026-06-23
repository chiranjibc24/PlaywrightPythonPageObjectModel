from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.amazon.in/s?k=iphone+17', wait_until='domcontentloaded')
    print('initial cart count', page.locator('#nav-cart-count').text_content())
    sel = "(//span[contains(text(),'iPhone 17')]/ancestor::div[@data-component-type='s-search-result']//button[@aria-label='Add to cart'])[1]"
    btn = page.locator(sel)
    print('button visible', btn.is_visible(), 'count', btn.count())
    if btn.is_visible():
        btn.click()
        page.wait_for_load_state('domcontentloaded')
        print('after click url', page.url)
        print('after cart count', page.locator('#nav-cart-count').text_content())
    else:
        print('btn not visible')
    browser.close()
