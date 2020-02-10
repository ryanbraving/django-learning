from django import template

register = template.Library()

@register.filter(name='cut_filter')
def cut_filter(value, arg):
    """
    This cuts out all values of "arg from the string
    """
    return value.replace(arg, '')

# register.filter("cut_filter", cut_filter)