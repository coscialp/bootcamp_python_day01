from book import Book
from recipe import Recipe


def main():
    gateau = Recipe("Gateau", 2, 35, ['egg', 'foul'], 'dessert')
    tarte = Recipe("tarte", 2, 20, ['egg', 'lol'], 'dessert', "C'est une tarte aux fraises")
    cookbook = Book('cookbook')
    cookbook.add_recipe(gateau)
    cookbook.add_recipe(tarte)
    cookbook.get_recipe_by_name('Gateau')
    recipes = cookbook.get_recipe_by_types('dessert')
    for recipe in recipes:
        print(recipe)


if __name__:
    main()

