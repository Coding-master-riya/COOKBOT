import csv
import os
from flask import Flask, render_template, request, jsonify

def create_app():
    app = Flask(__name__)

    # Define the path to the CSV file
    CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'recipes.csv')

    def load_recipes():
        recipes = []
        with open(CSV_FILE_PATH, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                recipe = {
                    'name': row['TranslatedRecipeName'],
                    'ingredients': row['Cleaned-Ingredients'].split(','),  # Use 'Cleaned-Ingredients' for better matching
                    'total_time': int(row['TotalTimeInMins']),
                    'cuisine': row['Cuisine'],
                    'instructions': row['TranslatedInstructions'],
                    'url': row['URL'],
                    'image_url': row['image-url'],
                    'ingredient_count': int(row['Ingredient-count'])
                }
                recipes.append(recipe)
        return recipes

    def find_recipes(ingredients):
        all_recipes = load_recipes()  # Load all recipes from the CSV
        matched_recipes = []

        # Split the input ingredients into a list and make them lowercase for comparison
        user_ingredients = [ingredient.strip().lower() for ingredient in ingredients.split(',')]

        print(f"User Ingredients: {user_ingredients}")  # Debugging line

        for recipe in all_recipes:
            # Make a list of ingredients for the recipe (lowercase for case-insensitive matching)
            recipe_ingredients = [ingredient.lower() for ingredient in recipe['ingredients']]

            # Check if all user ingredients are in the recipe's ingredients
            if all(user_ingredient in recipe_ingredients for user_ingredient in user_ingredients):
                matched_recipes.append(recipe)
                print(f"Matched Recipe: {recipe['name']}")  # Debugging line

        return matched_recipes

    # Home route - renders the homepage
    @app.route('/')
    def home():
        return render_template('index.html')  # Flask looks for this file in the templates folder

    # Search route - handles the AJAX request for searching recipes and returns JSON response
    @app.route('/search', methods=['POST'])
    def search():
        ingredients = request.form['ingredients']  # Get ingredients from the form data
        recipes = find_recipes(ingredients)  # Find matching recipes based on user input

        # Return JSON response with the recipe data
        return jsonify({'recipes': recipes})

    return app
