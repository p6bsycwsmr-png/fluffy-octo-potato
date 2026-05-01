# recipe_rec.py

import csv

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

        # Count matching ingredients
        matches = count_matches(user_ingredients, ingredients)

        # Find which ingredients are missing
        missing = find_missing(user_ingredients, ingredients)

        # Only keep recipes with more than 1 match
        if matches > 1:
            recommended.append([name, matches, missing])

    # Sort recipes by match count from highest to lowest
    recommended.sort(key=lambda recipe: recipe[1], reverse=True)

    # Keep only the top 5 recipes
    top_recipes = recommended[:5]

    # Print results
    print("\nHere are your top recipe matches:\n")

    if len(top_recipes) == 0:
        print("Sorry, no recipes matched well enough.")
    else:
        for recipe in top_recipes:
            print("Recipe:", recipe[0])
            print("Matches:", recipe[1])
            print("Missing ingredients:", recipe[2])
            print("-------------------------")


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