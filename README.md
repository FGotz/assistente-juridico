# ⚖️ AI Legal Assistant (Super Estagiário Jurídico)

An automated Legaltech tool built with Python and Object-Oriented Programming (OOP). This system reads legal documents (PDFs), analyzes the case using Google's Gemini AI, and automatically drafts a formatted legal defense (Contestação) in Microsoft Word (.docx) format.

## 🎯 The Problem it Solves
Lawyers and legal teams spend hours reading initial petitions and formatting standard defense documents. This project automates the bureaucratic pipeline, acting as a virtual legal intern that extracts text from physical files, applies legal prompt engineering, and outputs a ready-to-use, formatted Word document.

## 🛠️ Technologies & Tools
* **Python (OOP):** Core logic structured using Object-Oriented Programming for modularity.
* **PyPDF2:** Used to read and extract raw text from PDF files.
* **python-docx:** Used to programmatically generate Microsoft Word documents with strict legal formatting (Arial, Size 12, Justified text, bold headers).
* **Google Gemini AI (genai):** LLM integration via API to analyze facts and draft the legal defense structure (Preliminary, Merit, and Requests).
* **python-dotenv:** Secure environment variable management to protect API keys.

## ⚙️ Architecture
The system is built around the `AssistenteJuridico` class, containing three specialized workers:
1. `extrair_texto()`: The "Eyes" - Reads the PDF and extracts strings.
2. `redigir_defesa()`: The "Brain" - Sends the text and a strict legal prompt to Gemini.
3. `formatar_word()`: The "Hands" - Takes the AI's output and formats it into a standard `.docx` file.

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/SEU_USUARIO_AQUI/assistente-juridico.git](https://github.com/SEU_USUARIO_AQUI/assistente-juridico.git)
Install the required dependencies:

Bash
pip install PyPDF2 python-docx google-genai python-dotenv
Set up your environment variables:

Create a .env file in the root directory.

Add your Gemini API Key: GEMINI_API_KEY=your_api_key_here

Place a test PDF named processo_teste.pdf in the folder and run:

Bash
python sistema_juridico.py