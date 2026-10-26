
import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Text Summarization")
st.write(
    "Summarize long articles, notes, and paragraphs "
    "using Hugging Face Transformers."
)

@st.cache_resource(show_spinner="Loading the AI model...")
def load_model():
    return pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )

text = st.text_area(
    "Enter your text:",
    height=250,
    placeholder="Paste your article or study material here..."
)

length = st.selectbox(
    "Choose summary length",
    ["Short", "Medium", "Long"],
    index=1
)

settings = {
    "Short": {"min_length": 15, "max_length": 50},
    "Medium": {"min_length": 30, "max_length": 100},
    "Long": {"min_length": 50, "max_length": 150}
}

if st.button("Generate Summary", type="primary"):
    if len(text.split()) < 30:
        st.warning("Please enter at least 30 words.")
    else:
        try:
            with st.spinner("Generating your summary..."):
                summarizer = load_model()

                result = summarizer(
                    text,
                    **settings[length],
                    do_sample=False,
                    truncation=True
                )

                summary = result[0]["summary_text"]

            st.subheader("Generated Summary")
            st.success(summary)

            st.write("Original word count:", len(text.split()))
            st.write("Summary word count:", len(summary.split()))

            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Error: {e}")
            st.write(
                "Check your internet connection and "
                "confirm that all packages installed correctly."
            )