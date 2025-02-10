import pytest
from selene import browser, be, have

@pytest.fixture()#scope='session')
def setting_browser():
    browser.config.window_width = 1920  # задает ширину окна браузера
    browser.config.window_height = 1080  # задает высоту окна браузера
    yield
    browser.quit() # закрывает браузер после выполнения теста
    print('Браузер закрывается') #teardown


def test_first(setting_browser):
    browser.open("https://duckduckgo.com")
    browser.element('[name="q"]').should(be.blank).type('prothai.live').press_enter()
    browser.element('html').should(have.text('Самые актуальные новости о Тайланде'))

def test_second(setting_browser):
    browser.open("https://duckduckgo.com")
    browser.element('[name="q"]').should(be.blank).type('#4@^$@#&59@65(@#*&$612345').press_enter()
    browser.element('html').should(have.text('Free math'))

def test_second_one(setting_browser):
    browser.open("https://duckduckgo.com")
    browser.element('[name="q"]').should(be.blank).type('#4@^$@#&59@65(@#*&$612345').press_enter()
    browser.element('html').should(have.text('#4@^$@#&59@65(@#*&$612345'))

def test_third(setting_browser):
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').should(be.blank).type('prothai.live').press_enter()
    browser.element('html').should(have.text('Об этой странице'))
