# Assessment Recommender System (RAG-Based)

A high-performance **Retrieval-Augmented Generation (RAG)** system that intelligently recommends **SHL assessments** from natural-language queries. By combining semantic vector search with **Google Gemini 1.5 Flash**, the system delivers context-aware, explainable, and production-ready recommendations.

🔗 [Live Demo](https://jclg3riyas8cdlxmcdfcxs.streamlit.app/) | 📺 [Watch Demo Video](https://www.google.com/search?q=images/working_vedio.mp4)

---

## 🚀 Key Features

* **🔍 Semantic Retrieval**: Uses `SentenceTransformers (all-MiniLM-L6-v2)` and **FAISS** to understand user intent beyond simple keyword matching.
* **🤖 AI-Powered Explanations**: Integrates **Google Gemini 1.5 Flash** to generate natural-language justifications for every recommendation.
* **🧱 Robust Data Pipeline**: Supports JSON, CSV, and Excel with automated normalization and regex-based metadata extraction (e.g., test duration).
* **🔄 Hybrid Output Design**: Provides human-readable summaries for users and structured JSON for API integrations.
* **🧪 Built-in Evaluation**: Features a dedicated module for **Recall@K** metrics to validate embedding quality and retrieval accuracy.
* **🛡 Reliable Fallback**: Gracefully degrades to raw semantic search results if the LLM API is unavailable or rate-limited.

---

## 📸 Screenshots & Demo

### 🔹 System Architecture (RAG Flow)

High-level overview of the ingestion, embedding, retrieval, and LLM augmentation layers.

<p align="center">
<img src="images/data_flow.png" alt="System Architecture" width="800">
</p>

### 🔹 Streamlit Web Interface

The interactive UI allows users to input job descriptions or skill requirements to find matching assessments.

<p align="center">
<img src="images/web_view.png" alt="Web Interface" width="800">
</p>

---

## 🧠 System Architecture (High-Level)

1. **Ingestion Layer**: Loads the SHL catalog, cleans data, and creates combined text fields for indexing.
2. **Embedding & Vector Store**: Generates dense embeddings and stores them in **FAISS** for millisecond similarity search.
3. **RAG Engine**: Retrieves top-K relevant assessments and enriches the prompt context for the LLM.
4. **Evaluation Module**: Computes **Recall@K** to ensure the most relevant tests are always surfacing.

---

## 📁 Project Structure

```bash
Assessment-Recommender-System/
├── data/
│   ├── shl_products.json     # Source assessment catalog
│   └── faiss_index/          # FAISS vector store
├── images/                   # Screenshots & diagrams
├── outputs/                  # Evaluation reports & JSON logs
├── src/                      # Core Source Code
│   ├── config.py             # Global configuration & Hyperparameters
│   ├── embeddings/           # Vectorization logic
│   ├── ingestion/            # Data cleaning & regex extraction
│   ├── rag/                  # Core RAG engine & Gemini integration
│   └── evaluation/           # Recall@K evaluation scripts
├── requirements.txt
└── .env                      # API keys (Gemini)

```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yashmishra1234567890/Assessment-Recommender-System.git
cd Assessment-Recommender-System

```

### 2️⃣ Environment Setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate | Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt

```

### 3️⃣ Configure API Key

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here

```

---

## ▶️ Usage

### 🔹 Run the Recommendation Engine

Test the RAG pipeline via the CLI:

```bash
python src/rag/rag_engine.py

```

### 🔹 Run Retrieval Evaluation

Validate the accuracy of the vector search:

```bash
python src/evaluation/run_eval.py

```

*Results are saved to `outputs/evaluation_results.csv`.*

---

## 🛠 Tech Stack

| Category | Technology |
| --- | --- |
| **Language** | Python 3.12 |
| **LLM** | Google Gemini 1.5 Flash |
| **Vector DB** | FAISS |
| **Embeddings** | SentenceTransformers (HuggingFace) |
| **Orchestration** | LangChain |
| **Frontend** | Streamlit |

---

## 📌 Use Cases

* Automated SHL assessment matching from Job Descriptions (JDs).
* HR-tech platforms looking to automate skill-based discovery.
* GenAI-powered search and recommendation demos for recruitment.
