from django import template
import builtins

register = template.Library()

@register.filter
def repr(value):
    return builtins.repr(value)

@register.filter
def trim(value):
    return value.strip() if isinstance(value, str) else value


@register.filter
def safe_length(value):
    if hasattr(value, '__len__'):
        return len(value)
    return 0
