# dashboard_page.py
from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("h1")

    def navigate(self):
        self.page.goto("https://afton-quality-dashboard.s3.us-east-1.amazonaws.com/index.html")
    
    def get_heading_text(self):
        return self.page.inner_text("h1")