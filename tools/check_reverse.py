from django.template import engines, Context

print('Testing template reverse for recipes:home and recipes:search')
try:
    t=engines['django'].from_string("{% url 'recipes:home' as h %}home={{h}}")
    print('home =>', t.render({}))
except Exception as e:
    print('home reverse error', e)

try:
    t=engines['django'].from_string("{% url 'recipes:search' as s %}search={{s}}")
    print('search =>', t.render({}))
except Exception as e:
    print('search reverse error', e)
