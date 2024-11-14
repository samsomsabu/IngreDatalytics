import streamlit as st
import pandas as pd
import os
from src.processing import clean_recipe_data

def load_data():
    cleaned_data_path = 'D:/Project1/data/processed/cleaned_recipes.csv'
    return pd.read_csv(cleaned_data_path)

def main():
    st.title('Trending Recipe Ingredients')
    
    # Clean the data if it's not already cleaned
    if not os.path.exists('D:/Project1/data/processed/cleaned_recipes.csv'):
        st.write("Cleaning the data...")
        clean_recipe_data()
        st.write("Data cleaned and saved!")

    # Load the cleaned data
    df = load_data()

    st.write("Displaying the cleaned recipe data:")
    st.dataframe(df)

    # Optionally, you can add more analysis or visualizations here, such as word cloud of ingredients.

if __name__ == "__main__":
    main()
