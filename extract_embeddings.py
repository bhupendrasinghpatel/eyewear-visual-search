import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import pandas as pd
import numpy as np

# Load metadata
df = pd.read_csv("metadata.csv")

# Load pretrained ResNet50
model = models.resnet50(pretrained=True)
model.fc = torch.nn.Identity()   # remove final classifier
model.eval()

# Image preprocessing pipeline
transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225])
])

embeddings = []

for path in df["image_path"]:
    img = Image.open(path).convert("RGB")
    img = transform(img).unsqueeze(0)

    with torch.no_grad():
        vector = model(img).numpy().flatten()

    embeddings.append(vector)

embeddings = np.array(embeddings)

np.save("embeddings.npy", embeddings)

print("Saved embeddings.npy with shape", embeddings.shape)
