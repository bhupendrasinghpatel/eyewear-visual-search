import os
import faiss
import numpy as np
import pandas as pd
from PIL import Image
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from attributes import detect_style


# -----------------------------
# Load Data
# -----------------------------
metadata = pd.read_csv("metadata.csv")
embeddings = np.load("embeddings.npy")

dimension = embeddings.shape[1]

# Build FAISS index
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


# -----------------------------
# Load Pretrained Model
# -----------------------------
model = models.resnet50(pretrained=True)
model.fc = torch.nn.Identity()
model.eval()

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225])
])


# -----------------------------
# Utility Functions
# -----------------------------
def get_embedding(image_path):
    img = Image.open(image_path).convert("RGB")
    img = transform(img).unsqueeze(0)

    with torch.no_grad():
        vector = model(img).numpy().flatten()

    return vector.reshape(1, -1)


def load_clicks():
    if os.path.exists("click_log.csv"):
        return pd.read_csv("click_log.csv")
    return pd.DataFrame(columns=["product_id", "clicks"])


def record_click(product_id):
    clicks = load_clicks()

    if product_id in clicks["product_id"].values:
        clicks.loc[clicks["product_id"] == product_id, "clicks"] += 1
    else:
        clicks.loc[len(clicks)] = [product_id, 1]

    clicks.to_csv("click_log.csv", index=False)


# -----------------------------
# MAIN SEARCH FUNCTION
# -----------------------------
def search(image_path, k=5, category=None):
    """
    image_path : query image path
    k          : number of similar items
    category   : optional filter (Eyeglasses / Sunglasses)
    """

    # Get query embedding
    query_vector = get_embedding(image_path)

    # KNN search
    distances, indices = index.search(query_vector, k)

    # Retrieve metadata
    results = metadata.iloc[indices[0]].copy()

    # Add product id
    results["product_id"] = results.index

    # Attribute Prediction
    results["predicted_style"] = results["image_url"].apply(detect_style)

    # Similarity
    results["similarity_score"] = distances[0]

    # Load Feedback Clicks
    clicks = load_clicks()
    results = results.merge(clicks, on="product_id", how="left")
    results["clicks"] = results["clicks"].fillna(0)

    # Boost Scores
    results["boosted_score"] = results["similarity_score"] - (results["clicks"] * 0.5)

    # Apply optional filter
    if category:
        results = results[results["category"] == category]

    # Sort
    results = results.sort_values("boosted_score")

    return results
