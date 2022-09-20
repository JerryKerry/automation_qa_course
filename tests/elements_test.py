import pages.base_page



def test(driver):
    page = pages.base_page.BasePage(driver, 'https://www.google.com')
    page.open()


