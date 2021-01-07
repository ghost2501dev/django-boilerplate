from unittest import mock

from django.urls import reverse

from ..views import change_language


def _test_change_language_should_change_the_language(activate_mock, response):
    assert activate_mock.call_args_list[1][0][0] == 'es'
    assert response.client.cookies['language_code'].value == 'es'


@mock.patch('django.utils.translation.activate')
def test_change_language_should_change_the_language_and_return_204(activate_mock, client):
    url = reverse('change-language')
    response = client.post(url, {'language': 'es'})
    _test_change_language_should_change_the_language(activate_mock, response)
    assert response.status_code == 204


@mock.patch('django.utils.translation.activate')
def test_change_language_should_change_the_language_and_redirect(activate_mock, client):
    url = reverse('change-language')
    response = client.post(url, {'language': 'es', 'redirect_to': '/'}, follow=True)
    _test_change_language_should_change_the_language(activate_mock, response)
    last_url, status_code = response.redirect_chain[0]
    assert last_url == '/'
    assert status_code == 302
