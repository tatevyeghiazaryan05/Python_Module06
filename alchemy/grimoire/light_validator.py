def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    ingredients = ingredients.lower()
    items = ingredients.split(",")
    for i in items:
        if i.strip() in allowed:
            return "VALID"
    return "INVALID"
