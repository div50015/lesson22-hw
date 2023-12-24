import allure
import pytest
import allure_commons
from lesson22_hw.utils import allure_attach
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from selene import browser, support
from appium import webdriver


def pytest_addoption(parser):
    parser.addoption("--context", default="bstack", help="Specify context")


def pytest_configure(config):
    context = config.getoption("--context")
    load_dotenv(dotenv_path=f'.env.{context}')


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management(context):
    from configuration import settings

    options = UiAutomator2Options().load_capabilities(settings.to_driver_options(context=context))

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            settings.remote_url,
            options=options
        )

    browser.config.timeout = 10.0

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    allure_attach.attach_bstack_screenshot()
    allure_attach.attach_bstack_page_source()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    if context == 'bstack':
        allure_attach.attach_bstack_video(settings, session_id)
