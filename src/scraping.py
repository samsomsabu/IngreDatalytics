import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import time

def get_trending_recipes(url="https://www.allrecipes.com/"):
    # Ensure the data/raw directory exists
    raw_data_folder = 'D:/Project1/data/raw'
    os.makedirs(raw_data_folder, exist_ok=True)

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page {url} with status code {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate recipe links with an updated selector
    recipe_links = [a['href'] for a in soup.select('a.fixed-recipe-card__title-link')]

    print(f"Found {len(recipe_links)} recipe links")  # Debugging step

    recipes = []
    for link in recipe_links:
        recipe_data = scrape_recipe(link)
        if recipe_data:
            recipes.append(recipe_data)
            time.sleep(1)  # Avoid rapid requests to the server

    if recipes:
        # Convert to DataFrame and save to CSV
        recipe_df = pd.DataFrame(recipes)
        recipe_df.to_csv(f'{raw_data_folder}/recipes.csv', index=False)
        print("Scraping completed and saved to D:/Project1/data/raw/recipes.csv")
    else:
        print("No recipes scraped.")

    return recipes

def scrape_recipe(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve recipe page {url} with status code {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        # Get recipe title
        title = soup.find("h1", class_="headline heading-content").text.strip()

        # Get recipe ingredients
        ingredients = [ingredient.text.strip() for ingredient in soup.select("span.ingredients-item-name")]

        # Debugging: print title and ingredients
        print(f"Scraping recipe: {title}")
        print(f"Ingredients: {ingredients}")

        return {
            "title": title,
            "ingredients": ingredients,
            "date_scraped": datetime.now().strftime('%Y-%m-%d')
        }
    except AttributeError:
        print(f"Error scraping recipe: {url}")
        return None

# Run the scraping function if this script is executed directly
if __name__ == "__main__":
    get_trending_recipes("https://www.allrecipes.com/")
