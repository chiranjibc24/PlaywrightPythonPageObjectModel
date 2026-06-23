from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.amazon.in/s?k=iphone+17', wait_until='domcontentloaded')
    page.wait_for_timeout(10000)
    print('page url:', page.url)
    print('body contains search-result:', 'data-component-type="s-search-result"' in page.content())
    print('body starts:', page.content()[:2000])
    browser.close()
