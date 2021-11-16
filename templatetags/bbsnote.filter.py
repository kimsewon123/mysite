# 게시물 번호공식 
from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg