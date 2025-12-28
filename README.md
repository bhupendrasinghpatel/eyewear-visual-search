🕶️ Eyewear Visual Search 🔍🤖
AI-Powered Image Similarity Search for Glasses & Sunglasses
🌟 Overview

The Eyewear Visual Search project is an AI-driven platform that allows users to upload an image of eyewear and instantly discover visually similar frames from a product catalog.

Instead of searching with text keywords like “thin gold rectangular semi-rim glasses”, users simply upload an image — and the system finds look-alike styles using deep learning & vector similarity search.

The goal is to enable Search-by-Image shopping — similar to Amazon / Google Lens — but focused on eyewear.

🚀 Features

🖼️ Upload an eyewear image
🔍 AI-powered visual similarity search
🧠 Frame style recognition (Cat-Eye, Rectangle, Round, etc.)
🧾 Product catalog metadata (category, link, etc.)
📊 Similarity score in percentage
🗂 Filtering by category (Eyeglasses / Sunglasses)
⚡ Fast retrieval using FAISS vector search
👍 User feedback ranking (click boosting)
🌐 Simple, clean web UI
🧱 Modular ML pipeline
🔥 Production-style architecture

🛠️ Tech Stack
🎨 Frontend

HTML5

CSS3

JavaScript

⚙️ Backend

Flask (Python)

REST APIs

CORS enabled

🧠 AI Engine

ResNet-50 CNN (TorchVision pretrained)

Image Embedding Extraction

Cosine/L2 Vector Similarity

📦 Vector Database

FAISS (Facebook AI Similarity Search)

📂 Data

metadata.csv (products & URLs)

embeddings.npy (feature vectors)

📂 Architecture
🔧 Workflow

1️⃣ User uploads eyewear image
2️⃣ System preprocesses & extracts embeddings
3️⃣ FAISS finds nearest neighbor matches
4️⃣ Results ranked + similarity % calculated
5️⃣ User feedback logged
6️⃣ Search quality improves over time

📊 System Flow
User Upload  →  Flask API
                 ↓
         Preprocessing (resize/normalize)
                 ↓
     CNN Embedding Extraction (ResNet-50)
                 ↓
       Vector Search using FAISS Index
                 ↓
     Rank + Compute Similarity Percentage
                 ↓
     Attribute Classification (Frame Style)
                 ↓
         JSON Response to Frontend
                 ↓
     Frontend Displays Recommendations

🔍 Output Example
{
  "category": "Eyeglasses",
  "predicted_style": "Rectangle",
  "similarity": "92.5%",
  "image_url": "https://example.com/frame.jpg",
  "product_id": 637
}

🧠 AI Strategy

The project uses a pretrained ResNet-50 CNN as a feature extractor:

✔ Remove final classification head
✔ Extract 2048-dim embedding
✔ Store vectors in FAISS index

Similarity is computed using:

Similarity % = 100 − boosted_score


Where:

boosted_score = distance − (clicks × weight)


So relevant items move higher with user feedback 👍

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/eyewear-visual-search.git
cd eyewear-visual-search

2️⃣ Install Dependencies
pip install -r requirements.txt



3️⃣ Run Backend
python app.py


API runs at:

👉 http://127.0.0.1:5000

4️⃣ Run Frontend
python -m http.server 8000


Open:

👉 http://127.0.0.1:8000/frontend.html

🖥️ Screenshots (Optional Section)
<img width="1894" height="890" alt="Screenshot 2025-12-28 095606" src="https://github.com/user-attachments/assets/dd2e6ec6-614b-4700-ae4d-f1489c030f91" />
<img width="1885" height="884" alt="Screenshot 2025-12-28 095620" src="https://github.com/user-attachments/assets/f85362bc-ada0-4f0d-836d-bb028f951fc9" />
<img width="1894" height="879" alt="Screenshot 2025-12-28 095630" src="https://github.com/user-attachments/assets/1560d22f-4ff7-4aac-b0ad-151cec6d14ff" />
<img width="1892" height="671" alt="Screenshot 2025-12-28 095639" src="https://github.com/user-attachments/assets/5a7be8ce-9b74-441e-b814-3fde021a32c8" />



▶️ Usage

1️⃣ Upload eyewear photo
2️⃣ Select category (optional)
3️⃣ Click Find Similar Eyewear
4️⃣ View AI-generated recommendations
5️⃣ Click 👍 to mark relevant matches

📦 Example Use-Cases

👓 Replace broken glasses
🎥 Find celebrity eyewear
🛍️ Discover similar shopping styles
🤝 Fashion discovery tools


🙌 Acknowledgements

💙 PyTorch
💙 FAISS
💙 Flask
💙 Lenskart Product References
