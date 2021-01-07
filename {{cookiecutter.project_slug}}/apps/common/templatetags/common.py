from django import template
from django.conf import settings
from django.utils.translation import get_language_info as dj_get_language_info

register = template.Library()


@register.simple_tag
def get_settings(name):
    if name in settings.ALLOWABLE_TEMPLATE_SETTINGS:
        return getattr(settings, name, '')
    return ''


@register.simple_tag()
def get_language_info(lang_code):
    return dj_get_language_info(lang_code)
