import streamlit as st
import pickle
import os

# ===== Load Model Safely =====
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "..", "model", "best_sentiment_model.pkl")
model = pickle.load(open(model_path, "rb"))

# ===== Page Config =====
st.set_page_config(page_title="Sentiment Analyzer", page_icon="🎬", layout="centered")

# ===== Custom Styling =====
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #00C9A7;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #AAAAAA;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# ===== Title =====
st.markdown('<div class="title">🎬 Movie Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter a movie review and get sentiment prediction</div>', unsafe_allow_html=True)

# ===== Input Box =====
review = st.text_area(" Enter your movie review below:", height=150)

# ===== Predict Button =====
if st.button("🔍 Predict Sentiment"):
    if review.strip() != "":
        prediction = model.predict([review])[0]

        if prediction == "positive":
            st.success("Positive Review ")
        else:
            st.error(" Negative Review ")
    else:
        st.warning(" Please enter a review first")