<<<<<<< HEAD
print("Hello, Multilingual Misinformation Radar!")
=======
# Multilingual Misinformation Radar

## Project Overview

Multilingual Misinformation Radar is a beginner-friendly Data Science project built with Python and Streamlit. It creates a small dataset of social media-style posts in English, Hindi, and Telugu, analyzes misinformation labels, and displays the results in a simple dashboard.

The project uses rule-based keyword logic to classify a new post as Fake, Misleading, Real, or Low Risk.

## Tools Used

- Python
- pandas
- scikit-learn
- Streamlit
- openpyxl
- matplotlib

## Dataset Columns

The dataset is saved as `data/misinformation_posts.csv` and contains these columns:

- `post_id`: Unique ID for each post
- `username`: Name of the account that posted the content
- `post_text`: Text content of the post
- `language`: Language of the post
- `likes`: Number of likes
- `shares`: Number of shares
- `url`: Source URL for the post
- `label`: Category of the post, such as Fake, Real, or Misleading

## How to Run the Project

Install the required packages:

```bash
python3 -m pip install -r requirements.txt
```

Create the dataset:

```bash
python3 main.py
```

Run the analysis script:

```bash
python3 notebooks/analysis.py
```

Open the Streamlit dashboard:

```bash
python3 -m streamlit run app/app.py
```

## Key Features

- Creates a multilingual misinformation dataset
- Includes English, Hindi, and Telugu posts
- Uses Fake, Real, and Misleading labels
- Prints basic dataset summaries
- Analyzes label counts and language counts
- Shows fake and misleading posts separately
- Displays most shared URLs
- Calculates average likes and shares by label
- Provides a Streamlit dashboard with metrics and charts
- Allows filtering posts by language
- Classifies a new post using simple keyword-based rules

## Future Improvements

- Add a larger real-world dataset
- Train a machine learning model for classification
- Add more Indian languages
- Use natural language processing for better text analysis
- Add source credibility scoring
- Connect the dashboard to live social media or fact-checking data
>>>>>>> d8b9607 (Add analysis app and dataset files)
