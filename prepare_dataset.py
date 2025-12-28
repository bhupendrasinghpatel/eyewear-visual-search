import pandas as pd

# Load excel file
df = pd.read_excel("eyewear.xlsx")

rows = []

# Loop through each row
for i, r in df.iterrows():
    category = r["Category"]   # Eyeglasses / Sunglasses
    
    for col in df.columns:
        if "Image" in col and pd.notna(r[col]):
            rows.append({
                "category": category,
                "image_url": r[col]
            })

# Create new dataframe
clean_df = pd.DataFrame(rows)

# Save it
clean_df.to_csv("clean_metadata.csv", index=False)

print("Done! Saved clean_metadata.csv with", len(clean_df), "rows")
