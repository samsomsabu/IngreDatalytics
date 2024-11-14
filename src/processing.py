import pandas as pd
import os

def process_ingredients(ingredients):
    # Process ingredients: remove extra spaces, normalize text
    processed_ingredients = [ingredient.strip().lower() for ingredient in ingredients if ingredient.strip()]
    return processed_ingredients

def clean_recipe_data():
    # Load raw data from data/raw/recipes.csv
    raw_data_path = 'D:/Project1/data/raw/recipes.csv'
    processed_data_folder = 'D:/Project1/data/processed'
    
    # Create the processed folder if it doesn't exist
    os.makedirs(processed_data_folder, exist_ok=True)
    
    if not os.path.exists(raw_data_path):
        print(f"Raw data file not found: {raw_data_path}")
        return
    
    # Load the raw data
    raw_data = pd.read_csv(raw_data_path)

    # Clean ingredients using process_ingredients function
    raw_data['ingredients'] = raw_data['ingredients'].apply(lambda x: process_ingredients(eval(x)))

    # Basic cleaning steps (e.g., removing null values and duplicates)
    cleaned_data = raw_data.dropna(subset=['title', 'ingredients'])
    cleaned_data = cleaned_data.drop_duplicates(subset=['title'])

    # Save the cleaned data to processed folder
    cleaned_data_path = os.path.join(processed_data_folder, 'cleaned_recipes.csv')
    cleaned_data.to_csv(cleaned_data_path, index=False)

    print(f"Cleaned recipes saved to: {cleaned_data_path}")
    return cleaned_data

# Run the data cleaning function if this script is executed directly
if __name__ == "__main__":
    clean_recipe_data()
