from pathlib import Path

import pandas as pd

DATA_FILE = Path("data") / "misinformation_posts.csv"


def main():
    """Run simple pandas analysis on the misinformation dataset."""
    if not DATA_FILE.exists():
        print("Dataset not found.")
        print("Please run this command first: python3 main.py")
        return

    df = pd.read_csv(DATA_FILE)

    print("First 5 rows:")
    print(df.head())

    print("\nLabel counts:")
    print(df["label"].value_counts())

    print("\nLanguage counts:")
    print(df["language"].value_counts())

    print("\nFake posts only:")
    print(df[df["label"] == "Fake"])

    print("\nMisleading posts only:")
    print(df[df["label"] == "Misleading"])

    print("\nMost shared URLs:")
    print(df.sort_values(by="shares", ascending=False)[["url", "shares"]])

    print("\nAverage likes by label:")
    print(df.groupby("label")["likes"].mean())

    print("\nAverage shares by label:")
    print(df.groupby("label")["shares"].mean())

    print("\nLanguage-wise label count:")
    print(pd.crosstab(df["language"], df["label"]))


if __name__ == "__main__":
    main()
