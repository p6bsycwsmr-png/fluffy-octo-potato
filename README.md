# fluffy-octo-potato: cs32 final project

## an ingredient-based recipe recommender ##

My final project choice is a recipe recommendation tool that suggests meals based on ingredients a user already has at home. The program would take a list of ingredients as input, compare that list against a recipe dataset, and recommend recipes that best match the available ingredients. A more advanced version could also suggest ingredient substitutions or rank recipes by how few extra ingredients are needed.

## subtasks ##
* collect ingredient inputs from the user
* store or access a recipe dataset
* match available ingredients to possible recipes
* rank recipes by ingredient overlap
* suggest substitutions for missing ingredients
* display recipe recommendations

## FP Status Update ##
For my FP Status update, I've revised the simpler version of the recipe recommender to now include:
* a separate .csv file (recipes.csv) which holds all the possible recipes and ingredients -- this is much cleaner than writing up a dictionary within the main file and allows for us to 
* a ranked system that sorts the recommended recipes by number of ingredient matches
* 