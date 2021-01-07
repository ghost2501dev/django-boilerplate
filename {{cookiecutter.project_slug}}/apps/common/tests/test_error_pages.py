from core import urls

from ..views import bad_request, page_not_found, permission_denied, server_error


def test_bad_request_error(browser):
    assert urls.handler400 == 'common.views.bad_request'
    browser.visit('/error400/')
    assert browser.is_element_present_by_id('bad-request')
    assert browser.is_text_present('Bad request')
    assert browser.status_code.code == 400


def test_permission_denied_error(browser):
    assert urls.handler403 == 'common.views.permission_denied'
    browser.visit('/error403/')
    assert browser.is_element_present_by_id('permission-denied')
    assert browser.is_text_present('Permission denied')
    assert browser.status_code.code == 403


def test_page_not_found_error(browser):
    assert urls.handler404 == 'common.views.page_not_found'
    browser.visit('/error404/')
    assert browser.is_element_present_by_id('page-not-found')
    assert browser.is_text_present('Page not found')
    assert browser.status_code.code == 404


def test_server_error(browser):
    assert urls.handler500 == 'common.views.server_error'
    browser.visit('/error500/')
    assert browser.is_element_present_by_id('server-error')
    assert browser.is_text_present('Server error')
    assert browser.status_code.code == 500
