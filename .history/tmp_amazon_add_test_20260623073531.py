from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # use False for debugging
    page = browser.new_page()

    page.goto(
        "https://www.amazon.in/s?k=iphone+17",
        wait_until="networkidle",
        timeout=60000
    )

    print("Current URL:", page.url)
    print("Page Title:", page.title())

    page.locator("#nav-cart-count").wait_for(
        state="visible",
        timeout=60000
    )

    print(
        "Initial cart count:",
        page.locator("#nav-cart-count").text_content()
    )

    browser.close()