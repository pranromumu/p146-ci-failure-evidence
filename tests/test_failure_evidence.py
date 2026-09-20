from pathlib import Path
from playwright.sync_api import sync_playwright
artifact_dir = Path("artifact")
artifact_dir.mkdir(exist_ok=True)
def test_intentional_failure():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")
        screenshot_path = artifact_dir /"failure_evidence.png"
        page.screenshot(path=str(screenshot_path),full_page= True)
        assert "google" in page.title() , "Intentional failure to test CI evidence upload"
        browser.close()

