import pandas as pd
import requests
import os

# Load cleaned CSV
df = pd.read_csv("clean_metadata.csv")

# Make images folder
os.makedirs("images", exist_ok=True)

image_paths = []

for i, row in df.iterrows():
    url = row["image_url"]
    category = row["category"]

    filename = f"images/{category}_{i}.jpg"

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        with open(filename, "wb") as f:
            f.write(r.content)

        image_paths.append(filename)

    except Exception as e:
        print(f"Failed: {url}")
        image_paths.append(None)

df["image_path"] = image_paths
df = df.dropna()

df.to_csv("metadata.csv", index=False)

print("Download complete. Saved metadata.csv with", len(df), "images.")
