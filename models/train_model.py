from pathlib import Path
from io import StringIO

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


# Find the main project folder so this script works when we run:
# python3 models/train_model.py
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_ROOT / "data" / "misinformation_posts.csv"
MODEL_FILE = PROJECT_ROOT / "models" / "misinformation_model.pkl"


def load_dataset():
    # Read the CSV as text first so we can safely handle simple merge markers.
    csv_lines = DATA_FILE.read_text(encoding="utf-8-sig").splitlines()
    clean_lines = []
    header_seen = False

    for line in csv_lines:
        # Skip Git merge-conflict marker lines if they accidentally exist.
        if line.startswith(("<<<<<<<", "=======", ">>>>>>>")):
            continue

        # Keep the first header row and skip duplicate header rows.
        if line.startswith("post_id,username,post_text"):
            if header_seen:
                continue
            header_seen = True

        clean_lines.append(line)

    # Load the cleaned CSV text into a pandas DataFrame.
    return pd.read_csv(StringIO("\n".join(clean_lines)))


def main():
    # Check if the dataset file exists before trying to load it.
    if not DATA_FILE.exists():
        print("Dataset not found. Please run: python3 main.py")
        return

    # Load the misinformation dataset into a pandas DataFrame.
    df = load_dataset()
    print("Dataset loaded successfully")
    print(f"Dataset shape: {df.shape}")

    # Use post_text as the input feature for the machine learning model.
    x = df["post_text"]

    # Use label as the target output that the model should learn to predict.
    y = df["label"]

    # A Pipeline keeps the text converter and classifier together.
    model = Pipeline(
        [
            # TfidfVectorizer turns text into numbers the model can understand.
            ("tfidf", TfidfVectorizer()),
            # LogisticRegression is a beginner-friendly classification model.
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    # Train the model using the post text and labels.
    model.fit(x, y)

    # Check how well the model predicts the same training data.
    accuracy = model.score(x, y)
    print(f"Training accuracy: {accuracy:.2f}")

    # Save the trained model so the Streamlit app can use it later.
    joblib.dump(model, MODEL_FILE)


if __name__ == "__main__":
    main()
