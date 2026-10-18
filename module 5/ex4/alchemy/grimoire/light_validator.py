from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    allowed = light_spell_allowed_ingredients()

    if any(item in ingredients.lower() for item in allowed):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
