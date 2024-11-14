# Trending Recipe Ingredient Analysis

This project tracks trending ingredients from popular recipe websites. The pipeline scrapes, cleans, analyzes, and visualizes ingredient data.

## Project Structure
- `data/`: Stores raw and processed data files.
- `src/`: Contains core scripts for scraping, processing, analysis, and visualization.
- `app.py`: The main application script for Streamlit.

## Setup
1. Clone the repository and navigate to the directory:
    ```bash
    git clone https://github.com/your-username/trending-recipe-ingredients.git
    cd trending-recipe-ingredients
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the Streamlit app:
```bash
streamlit run app.py
