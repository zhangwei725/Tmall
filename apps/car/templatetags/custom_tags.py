from django import template

register = template.Library()


@register.filter
def get_ride_num(x, y):
    """
    计算两个值相乘
    :param x:
    :param y:
    :return:
    """
    return float(x) * float(y)
