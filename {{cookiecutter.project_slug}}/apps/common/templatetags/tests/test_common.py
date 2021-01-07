from django.conf import settings
from django.template import Context, Template


def test_get_settings():
    template = Template('{% load common %}{% get_settings "DEBUG" %}')
    rendered = template.render(Context())
    assert rendered == str(settings.DEBUG)


def test_get_language_info():
    template = Template('{% load common %}{% get_language_info "es" as language_info %}{{ language_info.code }}')
    rendered = template.render(Context())
    assert rendered == 'es'
