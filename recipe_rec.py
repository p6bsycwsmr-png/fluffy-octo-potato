# recipe_rec.py

import csv
from recipe_lib import *


"""
# Main function:
# - welcomes the user
# - loads recipes from the CSV file
# - gets user ingredients
# - prints recommendations
"""

def main():
    print("Welcome to the Recipe Recommender!\n")

    recipes = load_recipes("recipes.csv")
    user_ingredients = get_user_ingredients()

    print("\nYour ingredients:", user_ingredients)

    recommend_recipes(user_ingredients, recipes)

main()

if __name__ == main:
    main()