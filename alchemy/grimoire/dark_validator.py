from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ingredients = ingredients.lower()
    items = ingredients.split(",")
    for i in items:
        if i.strip() in allowed:
            return "VALID"
    return "INVALID"
