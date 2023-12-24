import lesson22_hw.utils.data
import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_wiki(context):
    allure.dynamic.parameter('context', context)
    check_txt = lesson22_hw.utils.data.set_check_text(context)

    with step('Verify content page 1'):
        results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        results.should(have.text(check_txt[0]))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Verify content page 2'):
        results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        results.should(have.text(check_txt[1]))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Verify content page 3'):
        results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        results.should(have.text(check_txt[2]))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Verify content page 4'):
        results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        results.should(have.text(check_txt[3]))
