from django import template

register = template.Library()


@register.simple_tag
def placeholder_url(width=870, height=541, template=None):
    """Retorna uma URL de imagem placeholder do picsum.photos com dimensões dadas.

    Uso no template:
        {% placeholder_url 320 240 as url %}
        <img src="{{ url }}">
    Ou direto:
        <img src="{% placeholder_url 320 240 %}">
    """
    try:
        w = int(width)
        h = int(height)
    except Exception:
        w, h = 870, 541

    if template:
        # substituir tokens {w} e {h} no template fornecido
        try:
            return template.format(w=w, h=h)
        except Exception:
            # se template inválido, cair para picsum
            pass

    return f"https://picsum.photos/{w}/{h}"
