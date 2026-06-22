# Multilingual Misinformation Radar

## Project Overview

Multilingual Misinformation Radar is a Data Science and NLP-based project that detects fake, misleading, and suspicious social media posts across English, Hindi, and Telugu.

The project analyzes multilingual social media-style posts, identifies misinformation patterns, detects suspicious URLs, and provides a Streamlit dashboard for easy visualization and prediction.

## Problem Statement

Misinformation spreads quickly on social media, especially in regional languages. Many fake posts are written in English, Hindi, Telugu, or mixed-language formats, making manual fact-checking difficult.

This project aims to help fact-checkers, analysts, and researchers quickly identify potentially fake or misleading posts using data analysis and machine learning.

## Features

* Multilingual dataset with English, Hindi, and Telugu posts
* Fake, Real, and Misleading label classification
* Data analysis of labels, languages, likes, shares, and URLs
* Streamlit dashboard for visualization
* Machine Learning model using TF-IDF and Logistic Regression
* New post prediction system
* Suspicious URL analysis
* Beginner-friendly project structure

## Tools and Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Joblib
* Matplotlib
* GitHub
* VS Code

## Project Structure

```text
Multilingual-Misinformation-Radar/
│
├── app/
│   └── app.py
│
├── data/
│   └── misinformation_posts.csv
│
├── models/
│   ├── train_model.py
│   └── misinformation_model.pkl
│
├── notebooks/
│   └── analysis.py
│
├── main.py
├── README.md
└── requirements.txt
```

## Dataset Columns

| Column    | Description                 |
| --------- | --------------------------- |
| post_id   | Unique ID of each post      |
| username  | User who posted the content |
| post_text | Social media post text      |
| language  | Language of the post        |
| likes     | Number of likes             |
| shares    | Number of shares            |
| url       | URL shared in the post      |
| label     | Fake, Real, or Misleading   |

## Machine Learning Approach

The ML model uses a Scikit-learn pipeline:

1. `TfidfVectorizer` converts text into numerical features.
2. `LogisticRegression` classifies the post as Fake, Real, or Misleading.
3. The trained model is saved as `models/misinformation_model.pkl`.

## How to Run the Project

Install the required libraries:

```bash
python3 -m pip install -r requirements.txt
```

Create the dataset:

```bash
python3 main.py
```

Run data analysis:

```bash
python3 notebooks/analysis.py
```

Train the machine learning model:

```bash
python3 models/train_model.py
```

Run the Streamlit dashboard:

```bash
python3 -m streamlit run app/app.py
```

## Dashboard Features

The dashboard displays:

* Total posts
* Fake posts
* Real posts
* Misleading posts
* Dataset preview
* Label distribution chart
* Language distribution chart
* Most shared URLs
* Language-wise filtering
* New post prediction using ML model

## Example Prediction

Input post:

```text
Government is giving free laptops to all students
```

Expected output:

```text
Prediction: Fake / High Risk
```

## Key Insights

* Fake posts are commonly related to free schemes, fake health cures, and suspicious links.
* Multilingual misinformation can appear in English, Hindi, Telugu, or mixed formats.
* Repeated URLs can indicate coordinated misinformation spreading.
* Posts with high shares and suspicious claims should be prioritized for fact-checking.

## Future Improvements

* Add a larger real-world misinformation dataset
* Add IndicBERT for better Hindi and Telugu NLP understanding
* Add Neo4j graph analysis to detect coordinated accounts
* Add LLaMA-based explanation generation
* Add real-time social media monitoring
* Add user and URL risk scoring

## Conclusion

This project demonstrates how data analysis, machine learning, and dashboarding can be combined to build a practical misinformation detection system. It is designed as a portfolio-worthy project for Data Science, NLP, Cybersecurity, and Analytics roles.
