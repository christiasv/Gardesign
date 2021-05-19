from django import template

register = template.Library()


@register.simple_tag
def set_indice(indice):
    return indice - 1


@register.simple_tag
def set_img(img):
    try:
        return img.url
    except Exception as e:
        return ''
