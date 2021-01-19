
from django import template

register = template.Library()

@register.simple_tag
def total_users():

    return 30

@register.simple_tag
def total_posts():

    return 23
