import streamlit as st
import joblib

st.set_page_config(
    page_title="AI-Powered Phishing Detection",
    page_icon="🛡️"
)

@st.cache_resource
def load_model():
    return joblib.load("phishing_detection_model.pkl")

st.title("🛡️ AI-Powered Phishing Detection")
st.write("Check a URL for potential phishing threats.")

url = st.text_input("Enter website URL")

if st.button("Check URL"):
    if not url.strip():
        st.warning("Please enter a URL.")
    else:
        st.info(
            "Input received. The trained model requires "
            "the same 54 features used during training. "
            "URL feature extraction must be connected "
            "before a reliable prediction can be displayed."
        )
