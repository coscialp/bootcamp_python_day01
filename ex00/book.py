from datetime import datetime
from recipe import Recipe


class Book:
    name = ""
    recipe_list = {
                    'starter': [],
                    'lunch': [],
                    'dessert': [],
                  }

    def __init__(self, name: str):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for value in self.recipe_list.values():
            for recipe in value:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print("ERROR: No recipe with this name")

    def get_recipe_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        if recipe_type != 'starter' and recipe_type != 'lunch' and recipe_type != 'dessert':
            print("ERROR: No recipe type with this name")
        return self.recipe_list[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        try:
            self.recipe_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
        except (TypeError, AttributeError):
            print("TypeError:   recipe must be a Recipe type")
            exit(0)

