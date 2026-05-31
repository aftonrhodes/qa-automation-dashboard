    # dashboard_page.py
from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        # Selectors
        self.table_rows = page.locator("#datatable tbody tr")
        self.name_input = page.locator("#input-name")
        self.email_input = page.locator("#input-email")
        self.submit_btn = page.locator("#submit-button")
        self.form_msg = page.locator("#form-message")
        self.status_checkbox = page.locator("#status-checkbox")
        self.status_label = page.locator("#status-label")

    def navigate(self):
        self.page.goto("https://afton-quality-dashboard.s3.us-east-1.amazonaws.com/index.html")

    def get_table_row_count(self):
        return self.table_rows.count()

    def submit_form(self, name, email):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.submit_btn.click()