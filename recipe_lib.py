## recipe_lib.py // a library holding all builder functions of recipe-rec.py

import csv

"""
# This function asks the user to type ingredients
# one at a time.
#
# The user types "done" when finished.
# Everything is changed to lowercase so matching
# is more consistent.
"""

def get_user_ingredients():
    print("Enter ingredients you have (type 'done' when finished):")

    user_ingredients = []

    while True:
        ingredient = input("> ").lower()

        if ingredient == "done":
            break

        user_ingredients.append(ingredient)

    return user_ingredients

"""
# This function loads recipe data from a CSV file.
# Each row in the file has:
# recipe name, ingredients
#
# The ingredients are stored in the CSV as one string
# separated by semicolons, so we split that string
# into a list.
"""

def load_recipes(filename):
    recipes = []

    with open(filename, newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip the header row

        for row in reader:
            name = row[0]
            ingredients = row[1].split(";")

            recipes.append([name, ingredients])

    return recipes

"""
# This function counts how many ingredients from
# the recipe appear in the user's ingredient list.
"""

def count_matches(user_ingredients, recipe_ingredients):
    count = 0

    for item in recipe_ingredients:
        if item in user_ingredients:
            count += 1

    return count

"""
# This function creates a list of ingredients that
# the user is missing for a recipe.
"""

def find_missing(user_ingredients, recipe_ingredients):
    missing = []

    for item in recipe_ingredients:
        if item not in user_ingredients:
            missing.append(item)

    return missing

"""
# This function calculates a recipe's match score 
# based on the percentage of recipe
# ingredients that the user already has.

# For example:
# - 3 matches out of 3 ingredients = 1.0
# - 3 matches out of 4 ingredients = 0.75

"""

def calculate_score(matches, total_ingredients):
    return matches / total_ingredients

"""
# This function finds recipes worth recommending.

# Rules:
# - Only include recipes with more than 1 match
# - Rank recipes from highest match count to lowest
# - Only show the top 5 recipes
"""

def recommend_recipes(user_ingredients, recipes):
    recommended = []

    # Go through every recipe in the dataset
    for recipe in recipes:
        name = recipe[0]
        ingredients = recipe[1]

        # Count how many ingredients match
        matches = count_matches(user_ingredients, ingredients)

        # Calculate percentage score
        score = calculate_score(matches, len(ingredients))

        # Only keep recipes with at least 50% match
        # This ensures recommendations are meaningful
        if score >= 0.5:
            missing = find_missing(user_ingredients, ingredients)

            # Store all relevant information in a list
            # [name, matches, score, missing ingredients]
            recommended.append([name, matches, score, missing])

    # Sort recipes by score from highest to lowest
    recommended.sort(key=lambda recipe: recipe[2], reverse=True)

    # Keep only the top 5 recipes
    top_recipes = recommended[:5]

    print("\nHere are your top recipe matches:\n")

    # If no recipes meet the requirement, print a message
    if len(top_recipes) == 0:
        print("Sorry, no recipes matched well enough.")
    else:
        # Print each recommended recipe clearly
        for recipe in top_recipes:
            print("Recipe:", recipe[0])
            print("Matches:", recipe[1])
            print("Score:", str(round(recipe[2] * 100, 1)) + "%")
            print("Missing ingredients:", recipe[3])
            print("-------------------------")