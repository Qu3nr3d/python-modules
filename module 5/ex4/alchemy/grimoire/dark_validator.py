from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str):
    allowed = dark_spell_allowed_ingredients()

    if any(item in ingredients.lower() for item in allowed):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
