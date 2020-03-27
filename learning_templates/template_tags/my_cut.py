from django import template

regiter=template.Library()

@regiter.filter(name='cut')
def cut(value,arg):
    """
    cuts the "arg" from the string.

    """
    return value.replace(arg,'')

# regiter.filter('cut',cut)
