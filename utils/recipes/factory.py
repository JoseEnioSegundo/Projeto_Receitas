# from inspect import signature
from random import randint
from datetime import datetime

try:
    from faker import Faker
except Exception:
    Faker = None


def rand_ratio():
    return randint(840, 900), randint(473, 573)


if Faker:
    fake = Faker("pt_BR")


def make_recipe():
    """Gera um dicionário de receita.

    Se o pacote `faker` não estiver disponível, usamos valores estáticos
    simples para não quebrar a importação do módulo em runtime.
    """
    if Faker:
        return {
            "title": fake.sentence(nb_words=6),
            "description": fake.sentence(nb_words=12),
            "preparation_time": fake.random_number(digits=2, fix_len=True),
            "preparation_time_unit": "Minutos",
            "servings": fake.random_number(digits=2, fix_len=True),
            "servings_unit": "Porção",
            "preparation_steps": fake.text(3000),
            "created_at": fake.date_time(),
            "author": {"first_name": fake.first_name(), "last_name": fake.last_name()},
            "category": {"name": fake.word()},
                "cover": {"url": "https://picsum.photos/%s/%s" % rand_ratio()},
        }

    # fallback simples quando faker não está instalado
    return {
        "title": "Receita Exemplo",
        "description": "Descrição gerada automaticamente.",
        "preparation_time": 30,
        "preparation_time_unit": "Minutos",
        "servings": 4,
        "servings_unit": "Porção",
        "preparation_steps": "Misture os ingredientes e cozinhe por 30 minutos.",
        "created_at": datetime.now(),
        "author": {"first_name": "João", "last_name": "Silva"},
        "category": {"name": "Outros"},
        "cover": {"url": "https://picsum.photos/%s/%s" % rand_ratio()},
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(make_recipe())