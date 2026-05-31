# test_dashboard.py
from dashboard_page import DashboardPage

def test_dashboard_loads(page):
    dashboard = DashboardPage(page)
    dashboard.navigate()
    assert dashboard.get_heading_text() == "Quality Assurance Dashboard"
