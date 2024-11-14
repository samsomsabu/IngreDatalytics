import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
#-----------------------------------------------------------
def plot_top_ingredients(trends_df, top_n=10):
    top_ingredients = trends_df.nlargest(top_n, 'frequency')
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_ingredients, x='frequency', y='ingredient')
    plt.title("Top Trending Ingredients")
    plt.xlabel("Frequency")
    plt.ylabel("Ingredient")
    plt.show()
#--------------------------------------------------------------
def plot_ingredient_trends(df, ingredient):
    # Filter for specified ingredient
    ingredient_data = df[df['ingredients'].apply(lambda x: ingredient in x)]
    trend_data = ingredient_data.groupby('date_scraped').size().reset_index(name='count')

    fig = px.line(trend_data, x='date_scraped', y='count', title=f"Trend for {ingredient}")
    fig.show()

#------------------------------------------------------------