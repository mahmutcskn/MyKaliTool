from playwright.sync_api import sync_playwright

def google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        page.fill("input[name='q']", "Kali Linux")
        page.press("input[name='q']", "Enter")
        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    google_search()
