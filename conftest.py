import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):

    parser.addoption(
        '--language',
        action='store',
        default='ru, en',  # или default=None,
        help='Language'
    )


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': language})
    driver = webdriver.Chrome(service=service, options=options)
    # driver.implicitly_wait(100)
    yield driver
    driver.quit()
