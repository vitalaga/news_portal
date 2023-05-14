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


@register.filter()
def hide_forbidden(value):
    words = value.split()
    result = []
    for word in words:
        if word in CURSE_WORDS:
            result.append(word[0] + "*" * (len(word) - 2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)
