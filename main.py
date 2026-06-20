import pandas as pd
import os

print("Starting Multilingual Misinformation Radar...")

# Create data folder if it does not exist
os.makedirs("data", exist_ok=True)

# Small sample dataset for our project
data = {
    "post_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "username": [
        "user_101", "user_102", "user_103", "user_104",
        "user_105", "user_106", "user_107", "user_108",
        "user_109", "user_110", "user_111", "user_112"
    ],
    "post_text": [
        "Government is giving free laptops to all students",
        "ప్రభుత్వం విద్యార్థులకు ఉచిత ల్యాప్‌టాప్‌లు ఇస్తోంది",
        "सरकार सभी छात्रों को मुफ्त लैपटॉप दे रही है",
        "IMD has issued a heavy rainfall alert for coastal areas",
        "రేపు భారీ వర్షాలు పడే అవకాశం ఉందని వాతావరణ శాఖ తెలిపింది",
        "आज बारिश की चेतावनी मौसम विभाग ने जारी की है",
        "Drink lemon water to cure dengue in one day",
        "నిమ్మరసం తాగితే డెంగ్యూ ఒక్క రోజులో తగ్గుతుంది",
        "नींबू पानी पीने से डेंगू एक दिन में ठीक हो जाएगा",
        "Government announced new scholarship application dates",
        "ప్రభుత్వం కొత్త స్కాలర్‌షిప్ దరఖాస్తు తేదీలను ప్రకటించింది",
        "सरकार ने नई छात्रवृत्ति आवेदन तिथियां घोषित की हैं"
    ],
    "language": [
        "English", "Telugu", "Hindi",
        "English", "Telugu", "Hindi",
        "English", "Telugu", "Hindi",
        "English", "Telugu", "Hindi"
    ],
    "likes": [120, 98, 150, 55, 70, 65, 210, 180, 190, 80, 75, 85],
    "shares": [45, 40, 60, 12, 18, 20, 95, 80, 85, 22, 20, 24],
    "url": [
        "http://fake-laptop.com",
        "http://fake-laptop.com",
        "http://fake-laptop.com",
        "http://weather.gov.in",
        "http://weather.gov.in",
        "http://weather.gov.in",
        "http://health-fake.com",
        "http://health-fake.com",
        "http://health-fake.com",
        "http://scholarship.gov.in",
        "http://scholarship.gov.in",
        "http://scholarship.gov.in"
    ],
    "label": [
        "Fake", "Fake", "Fake",
        "Real", "Real", "Real",
        "Misleading", "Misleading", "Misleading",
        "Real", "Real", "Real"
    ]
}

df = pd.DataFrame(data)

# Save dataset as CSV
df.to_csv("data/misinformation_posts.csv", index=False, encoding="utf-8-sig")

print("Dataset created successfully!")
print("\nFirst 5 rows:")
print(df.head())

print("\nShape of dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nLabel counts:")
print(df["label"].value_counts())

print("\nLanguage counts:")
print(df["language"].value_counts())

print("\nTop shared URLs:")
print(df["url"].value_counts())

print("\nCSV file saved at: data/misinformation_posts.csv")