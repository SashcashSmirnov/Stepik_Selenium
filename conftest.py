import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': language})
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def pytest_addoption(parser):

    parser.addoption(
        '--language',
        action='store',
        default='ru, en',
        help='Language'
    )
