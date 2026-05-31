from dashboard_page import DashboardPage

def test_dashboard_functionality(page):
    dashboard = DashboardPage(page)
    dashboard.navigate()

    # 1. Test Table
    assert dashboard.get_table_row_count() == 4
    
    # 2. Test Form
    dashboard.submit_form("Afton", "afton@test.com")
    assert dashboard.form_msg.is_visible()
    
    # 3. Test Toggle
    dashboard.status_checkbox.check()
    assert dashboard.status_label.inner_text() == "Online"