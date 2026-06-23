from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.amazon.in/s?k=iphone+17', wait_until='domcontentloaded')
    page.wait_for_timeout(10000)
    first = page.locator('[data-component-type="s-search-result"]').first
    print('first result has add button count', first.locator('button:has-text("Add to cart")').count())
    print('first result text snippet:', first.locator('h2').text_content())
    print('first result html:', first.inner_html()[:2000])
    print('first button aria-labels:')
    buttons = first.locator('button').all()
    for i,btn in enumerate(buttons[:10]):
        try:
            print(i, btn.get_attribute('aria-label'), btn.text_content())
        except Exception as e:
            print('button error', e)
    browser.close()
