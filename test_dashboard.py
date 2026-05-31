from playwright.sync_api import sync_playwright

def test_dashboard_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Replace this URL with your actual S3 Website Endpoint
        page.goto("https://afton-quality-dashboard.s3.us-east-1.amazonaws.com/index.html")
        
        # Verify the heading
        heading = page.inner_text("h1")
        assert heading == "Quality Assurance Dashboard"
        
        browser.close()
        print("Test passed: Dashboard loaded successfully!")