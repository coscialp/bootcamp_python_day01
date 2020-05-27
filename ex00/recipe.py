class Recipe:
    name = ""
    cooking_lvl = 0
    cooking_time = 0
    ingredients = []
    description = ""
    recipe_type = ""

    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, recipe_type: str,
                 description: str = ""):

        assert name and isinstance(name, str), "TypeError: name must be str type"
        assert cooking_lvl and isinstance(cooking_lvl, int), "TypeError: cooking_lvl must be int type"
        assert cooking_time and isinstance(cooking_time, int), "TypeError: cooking_time must be int type"
        assert ingredients and isinstance(ingredients, list), "TypeError: ingredients must be list type"
        assert recipe_type and isinstance(recipe_type, str), "TypeError: recipe_type must be str type"

        self.name = name
        if cooking_lvl in range(1, 5):
            self.cooking_lvl = cooking_lvl
        else:
            print("RangeError:  cooking_lvl must be in range 1 to 5")
            exit(0)
        if cooking_time > 0:
            self.cooking_time = cooking_time
        else:
            print("TimeError:  cooking_time can not be negative")
            exit(0)
        self.ingredients = ingredients
        if recipe_type == 'starter' or recipe_type == 'lunch' or recipe_type == 'dessert':
            self.recipe_type = recipe_type
        else:
            print("TypeError:  recipe_type can be “starter”, “lunch” or “dessert")
            exit(0)
        self.description = description

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "{}:\nLvl required: {}\n{}\nTime to cooked: {}\nList of ingredients: {}\nIt's for {}"

        return txt.format(self.name, self.cooking_lvl, self.description,
                          self.cooking_time, self.ingredients, self.recipe_type)
