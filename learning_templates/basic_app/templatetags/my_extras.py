from django import template

register = template.Library()


@register.filter(name="cut")
def cut(value, arg):
    """
    This cuts out all values of arg from the string!
    """
    return value.replace(arg, "")


# register.filter("cut", cut)
# better method for calling a function within function is through decorators.
# decorators come with@ symbol
