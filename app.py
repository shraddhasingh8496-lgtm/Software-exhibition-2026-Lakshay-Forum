import streamlit as st
import joblib

st.set_page_config(
    page_title="AI-Powered Phishing Detection",
    page_icon="🛡️"
)

@st.cache_resource
def load_model():
    return
    joblib.load("phishing_detection_model.pkl")

st.title("🛡️ AI-Powered Phishing Detection")
st.write("Check a URL for potential phishing threats.")

url = st.text_input("Enter website URL")

if st.button("Check URL"):
    if not url.strip():
        st.warning("Please enter a URL.")
    elif not os.path.exists("phishing_detection_model.pkl"):
        st.error("Model file missing!Please add"
                "phishing_detection_model.pkl to your repository.")
    else:
        try:
            model = load_model()
            st.success("model loaded succesfully!")
            st.info("URL feature extraction is not connected yet."
                    "A reliable phishing prediction cannot be made"
                    "Untill the required 54 features are extracted."
                   )
        except Exception as e:
            st.error(f"Model loading failed:{e}")
