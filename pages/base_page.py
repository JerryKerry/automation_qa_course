from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    """открываем браузер по конкретному url"""
    def open(self) :
        self.driver.get(self.url)

    """проверяем видимость элемента"""
    def element_is_visible(self, locator, timeout = 5):

        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    """проверяем видимость нескольких элементов"""
    def element_are_visible(self, locator,timeout = 5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    """Проверяем элемент по дом дереву , чтобы не скролитьт =)"""
    def element_is_present(self, locator,timeout = 5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    """Проверяем элементы  по дом дереву - много """
    def element_are_present(self, locator,timeout = 5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    """Ищем элементы  невидимый"""
    def element_is_not_visible(self, locator,timeout = 5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    """Проверяем на кликабельность """

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))


    """Скролим к нужному элементу"""

    def go_to_element(self, element):
        self.driver.executr_script("argument[0].scrollIntoView")




