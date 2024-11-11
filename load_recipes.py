import csv

recipes = []

# Open the CSV file
with open('recipes.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  # Automatically maps headers to dictionary keys
    
    for row in reader:
        recipe = {
            'name': row['TranslatedRecipeName'],
            'ingredients': row['TranslatedIngredients'].split(','),  # Assuming ingredients are separated by commas
            'total_time': int(row['TotalTimeInMins']),
            'cuisine': row['Cuisine'],
            'instructions': row['TranslatedInstructions'],
            'url': row['URL'],
            'image_url': row['image-url'],
            'ingredient_count': int(row['Ingredient-count'])
        }
        recipes.append(recipe)

# Print first recipe to verify
print(recipes[0])
