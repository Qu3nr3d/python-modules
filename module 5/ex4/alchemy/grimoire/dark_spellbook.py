from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients():
    return ["bats", "frogs", "arsenic", "eye-ball"]


def dark_spell_record(spell_name: str, ingredients: str):
    result = dark_validate_ingredients(ingredients)

    if result.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"
