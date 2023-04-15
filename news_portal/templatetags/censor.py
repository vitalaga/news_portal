from django import template

register = template.Library()

CURSE_WORDS = ['стратегия', 'направлений', 'исследователи', 'глупости', '']


@register.filter()
def censor(value):
    for word in CURSE_WORDS:
        if word in value:
            censor_word = ''.join(['*' for word in range(len(word))])
            value = value.replace(word, censor_word)
    return value
