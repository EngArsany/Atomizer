# 🚀 [Tips Hindawi](https://www.tipshindawi.com/) Internship (August–October) 2026

> 🎓 This project was built during the [**Tips Hindawi**](https://www.tipshindawi.com/) **Internship (August–October) 2026**.

## 👤 Participant

| Field            | Value                                |
| ---------------- | ------------------------------------ |
| Full Name        |  Arsany Hany Anwar                   |
| Project Name     |  Atomizer                            |
| GitHub Username  |  EngArsany                           |
| Internship Batch | August–October 2026                  |
| Training Program | Large Language Models (LLMs) Program |
| Organization     | [**Edrak for Ai**](https://edrak4ai.com/en)                         |

---

## 📖 Project Overview

Atomizer turns text based PDF documents into atomic knowledge notes. Upload a PDF in the Streamlit app and it sends the file to a FastAPI service, where a Mistral Nemo Instruct language model extracts distinct concepts and produces concise, self-contained notes. Each note is formatted as Markdown with tags and links to related notes, ready to add to an Obsidian-style knowledge base.

The current backend workflow is provided as a Kaggle notebook. The web app expects the backend to be running and reachable through the API settings described below.

---

## ✨ Features

* Upload PDF documents through a simple web interface.
* Extract text from PDFs and generate one note for each distinct concept.
* Format notes as Markdown with tags, related-note wiki links, and optional references.
* Display generated notes in the app and report API or connection errors.
* Protect the upload endpoint with a bearer token and enforce a 10 MB file-size limit.

---

## 🛠️ Technologies Used

* **Python 3.12+** for the application and backend workflow.
* **Streamlit** for the PDF upload and generated-note interface.
* **FastAPI** for the PDF processing API; the Kaggle notebook runs it with **Uvicorn** and exposes it through **ngrok**.
* **Mistral Nemo Instruct 2407** through **Transformers** and **PyTorch** for language-model generation.
* **PyPDF2** for PDF text extraction.
* **LangChain** output parsers and prompt templates to describe and structure note-generation output.
* **Requests** and **python-dotenv** for API calls and local configuration; **uv** for dependency management.

---

## ⚙️ Installation

1. Install Python 3.12 or newer and [uv](https://docs.astral.sh/uv/).
2. From the project root, install the declared dependencies:

   ```bash
   uv sync
   ```

3. Configure the frontend to reach a running backend by creating a `.env` file in the project root:

   ```dotenv
   API_URL=https://<your-backend-host>/upload-pdf/
   API_TOKEN=<your-bearer-token>
   ```

   The Kaggle notebook in `src/atomizer/notebook_kaggle.ipynb` contains the current backend workflow. Run it to load the model and start the FastAPI endpoint; set `API_URL` to its reachable `/upload-pdf/` URL and configure the same token on the backend. Keep credentials private.

4. Start the frontend:

   ```bash
   uv run streamlit run src/atomizer/app.py
   ```

---

## 🚀 Usage

1. Open the local Streamlit URL printed in the terminal.
2. Upload a text-based PDF (up to 10 MB).
3. Select **Generate Notes** and wait for the API to process the document.
4. Read the generated Markdown notes, including their tags and related-note links, in the results area.

Scanned PDFs may not produce usable text because the current extraction flow does not include OCR. The backend must be running and `API_URL` and `API_TOKEN` must match its configuration.

---

## 📸 Demo

Add screenshots, GIFs, or a demo video.

---

## 📈 Results

The project brings together a PDF upload interface and an LLM-backed processing workflow that returns structured, Markdown-formatted atomic notes. The Kaggle notebook demonstrates the end-to-end path from loading the model and extracting PDF text to generating and formatting linked notes. No benchmark or accuracy measurements are currently included.

---

## 🔮 Future Improvements

* Add a download or ZIP export for generated notes so they can be saved directly into a notes vault.
* Add OCR for scanned PDFs and improve extraction of tables, columns, and document structure.
* Migrate the UI to modern React if a richer, more interactive editing experience is needed.
* Add a flashcard creator based on the concepts in each generated note.
* Add persistent storage and retrieval so new notes can link to notes generated in earlier sessions.
* Validate and retry malformed model output, and provide clearer feedback for oversized, encrypted, or unsupported PDFs.
* Add source page references to notes and evaluate note quality on a documented test set.

---

## 📚 About the Internship

This project was developed as part of the [**Tips Hindawi**](https://www.tipshindawi.com/) **Internship (August–October) 2026**, and it will be showcased on the official [Tips Hindawi](https://www.tipshindawi.com/) website.

[Tips Hindawi](https://www.tipshindawi.com/) is the internships department of [**Edrak for Ai**](https://edrak4ai.com/en), and the internship encourages participants to build real-world projects, apply practical skills, and showcase their work through GitHub.

For more information about the internship, training programs, and upcoming batches, visit the official [Tips Hindawi](https://www.tipshindawi.com/) website.

---

## 📄 License

This project is shared for educational and portfolio purposes.

### Testing Data Sources

All sources used for testing were obtained from articles published by PLOS and are used in accordance with their applicable licenses. PLOS content is generally published under the Creative Commons Attribution (CC BY) license.

Source: [PLOS](https://plos.org/)
