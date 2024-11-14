import pandas as pd
from collections import Counter
#------------------------------------------------------
def calculate_ingredient_trends(df):
    # Flatten ingredient list and count occurrences
    all_ingredients = [ingredient for ingredients in df['ingredients'] for ingredient in ingredients]
    ingredient_counts = Counter(all_ingredients)

    # Convert to DataFrame for easier plotting
    trends_df = pd.DataFrame(ingredient_counts.items(), columns=['ingredient', 'frequency'])
    return trends_df
#-------------------------------------------
def load_data(input_file):
    return pd.read_csv(input_file)
#-------------------------------------------
