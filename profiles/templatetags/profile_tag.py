from django import template

from common.utils import get_profile

register = template.Library()

@register.simple_tag(takes_context=True, name='profile_tag')
def profile_buttons(context):
    if get_profile():
        return True
    return False
