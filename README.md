# 📄 Document Reader & Analyzer (Gemini API)
🚀 A **Streamlit web app** that allows users to upload PDFs or TXT files, extract text, and analyze it using **Google Gemini API** for summarization and Q&A.

## 🔹 Features
✅ Upload **PDF** or **TXT** files  
✅ Extract text automatically  
✅ Get AI-powered **summaries**  
✅ Ask questions about the document  
✅ Simple & interactive **UI**  

---

## ⚡ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```
   
2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

3.	**Install dependencies**
```bash
pip install -r requirements.txt
```

4.	**Set up Google Gemini API key**
Get your API key from Google AI Studio and set it in the script.
```python
import google.generativeai as genai
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

5. **🚀 Run the App**
```bash
streamlit run app.py
```

## 🛠 Technologies Used
- Streamlit – Interactive UI
- Google Gemini API – AI-powered text analysis
- PyMuPDF – PDF text extraction

## 💡 Future Enhancements
- ✅ Support for DOCX files
- ✅ Add metadata extraction
- ✅ Implement vector search for large documents


## 🙌 Contributing
- Fork the repository
- reate a new branch (feature-branch)
- Commit your changes
- Push to GitHub and open a Pull Request

### 👨‍💻 Author

👤 Arpit Patel(arpitaa9918@gmail.com)

🌟 If you like this project, give it a star ⭐ on GitHub!

---
