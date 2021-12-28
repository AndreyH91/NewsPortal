from django import template


register = template.Library()


@register.filter(name='censor')
def censor(value):
    censor_list = ['мат', 'дурак', 'фигня']
    text = value.split()
    for word in text:
        if word.lower() in censor_list:
            value = value.replace(word, '[CENSORED]')
    return value

