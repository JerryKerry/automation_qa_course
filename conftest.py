
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

"""функция которая создаёт драйвер, открывает его и после выполнения теста закрывает"""
@pytest.fixture(scope='function')
def driver():
    """Команда запускает браузер"""
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


