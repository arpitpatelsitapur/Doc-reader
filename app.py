import streamlit as st
import google.generativeai as genai
import fitz  # PyMuPDF for PDF processing

# Configure Gemini API Key
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Function to extract text from a PDF file
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = "\n".join(page.get_text() for page in doc)
    return text

# Function to analyze document using Gemini API
def analyze_text(text, task="Summarize"):
    prompt = f"{task} this document:\n{text}"
    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="Doc Analyzer", layout="wide")
st.title("📄 Document Reader & Analyzer")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    # Extract text from uploaded file
    if uploaded_file.type == "application/pdf":
        document_text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "text/plain":
        document_text = uploaded_file.read().decode("utf-8")

    # Display extracted text
    with st.expander("🔍 Extracted Text Preview", expanded=False):
        st.text_area("Document Content", document_text, height=300)

    # Select operation: Summarization or Q&A
    task_option = st.radio("Select Operation:", ["Summarize", "Ask a Question"])

    if task_option == "Summarize":
        if st.button("Summarize Document"):
            summary = analyze_text(document_text, task="Summarize")
            st.subheader("📌 Document Summary")
            st.write(summary)

    elif task_option == "Ask a Question":
        user_question = st.text_input("Enter your question about the document:")
        if st.button("Get Answer"):
            if user_question:
                answer = analyze_text(f"Answer this question based on the document: {user_question}\n{document_text}")
                st.subheader("🤖 AI Response")
                st.write(answer)
            else:
                st.warning("Please enter a question.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Arpit Patel")
