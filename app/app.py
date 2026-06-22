from pathlib import Path

import pandas as pd
import streamlit as st


DATA_FILE = Path("data") / "misinformation_posts.csv"


def classify_post(post_text):
    """Classify a post using simple beginner-friendly keyword rules."""
    text = post_text.lower()

    fake_keywords = [
        "miracle",
        "cure",
        "overnight",
        "guaranteed",
        "fake",
        "कैंसर",
        "ठीक",
        "నయమవుతుంది",
        "ఎప్పటికీ",
    ]
    misleading_keywords = [
        "breaking",
        "claim",
        "sources",
        "ban",
        "free",
        "मुफ्त",
        "घोषणा",
        "వార్తలు",
        "ఉద్యోగాలు",
    ]
    real_keywords = [
        "announced",
        "department",
        "official",
        "warning",
        "update",
        "चेतावनी",
        "जारी",
        "ప్రకటించారు",
        "తేదీలు",
    ]

    if any(keyword in text for keyword in fake_keywords):
        return "Fake"
    if any(keyword in text for keyword in misleading_keywords):
        return "Misleading"
    if any(keyword in text for keyword in real_keywords):
        return "Real"
    return "Low Risk"


def main():
    st.set_page_config(page_title="Multilingual Misinformation Radar", layout="wide")
    st.title("Multilingual Misinformation Radar")

    if not DATA_FILE.exists():
        st.error("Dataset not found. Please run `python3 main.py` first.")
        return

    df = pd.read_csv(DATA_FILE)

    total_posts = len(df)
    fake_posts = (df["label"] == "Fake").sum()
    real_posts = (df["label"] == "Real").sum()
    misleading_posts = (df["label"] == "Misleading").sum()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Posts", total_posts)
    col2.metric("Fake Posts", fake_posts)
    col3.metric("Real Posts", real_posts)
    col4.metric("Misleading Posts", misleading_posts)

    st.subheader("Dataset Preview")
    st.dataframe(df, use_container_width=True)

    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        st.subheader("Label Distribution")
        st.bar_chart(df["label"].value_counts())

    with chart_col2:
        st.subheader("Language Distribution")
        st.bar_chart(df["language"].value_counts())

    st.subheader("Most Shared URLs")
    most_shared = df.sort_values(by="shares", ascending=False)[
        ["url", "language", "label", "shares"]
    ]
    st.dataframe(most_shared, use_container_width=True)

    st.subheader("Filter Posts by Language")
    languages = ["All"] + sorted(df["language"].unique().tolist())
    selected_language = st.selectbox("Choose a language", languages)

    if selected_language == "All":
        filtered_df = df
    else:
        filtered_df = df[df["language"] == selected_language]

    st.dataframe(filtered_df, use_container_width=True)

    st.subheader("Check a New Post")
    user_post = st.text_area("Enter a post to classify")

    if user_post:
        result = classify_post(user_post)
        st.write(f"Prediction: **{result}**")

    st.subheader("Key Insights")
    most_common_label = df["label"].value_counts().idxmax()
    most_common_language = df["language"].value_counts().idxmax()
    highest_shared_post = df.loc[df["shares"].idxmax()]

    st.write(f"- Most common label in this dataset: **{most_common_label}**")
    st.write(f"- Most common language in this dataset: **{most_common_language}**")
    st.write(
        "- Most shared post URL: "
        f"**{highest_shared_post['url']}** "
        f"with **{highest_shared_post['shares']}** shares"
    )
    st.write(
        "- Keyword rules are useful for learning, but a real misinformation radar "
        "would need a trained machine learning model and verified fact-checking data."
    )


if __name__ == "__main__":
    main()
