# from django import template
#
#
# register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются
#
#
# @register.filter(name='multiply')  # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
# def multiply(value, arg):  # первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|multiply:arg
#     if isinstance(value, str) and isinstance(arg, int):
#         return str(value) * arg
#     else:
#         raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}')


