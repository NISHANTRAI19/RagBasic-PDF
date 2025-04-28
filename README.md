NAMASTE!!!
## Overview
This project allows you to ingest a PDF file into a vector database and interact with it using a retriever agent. It uses a local Qdrant instance for vector storage and Gemini API for generating responses.



## Setup Instructions

### 1. Create a Python Virtual Environment 
```bash (in your terminal run these commands)
python -m venv myenv
myenv\Scripts\activate  # For Windows
```

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```

### 3. Start Docker Services
Ensure Docker is installed and running on your machine.
Start the services defined in `docker-compose.yml`:
```bash
docker compose -f docker-compose.yml up
```
This will start a local Qdrant instance at `http://localhost:6333`.

---

## Data Ingestion

### 4. Update PDF File Name
Open `ingestion.py` and **change the name/path of the PDF file** you want to ingest.

### 5. Run the Ingestion Script (One-Time)
```bash
python ingestion.py
```
This step processes and stores the document embeddings into Qdrant.

---

## Chat with the Agent

### 6. Run the Retriever
```bash
python retriever.py
```
You can now retrieve information and chat with the agent based on the ingested document.

---

## Environment Variables

Create a `.env` file in the project root with the following contents:
```bash
GEMINI_API_KEY="YOUR_API_KEY"
QDRANT_LINK="http://localhost:6333"
```
- **GEMINI_API_KEY**: Your API key for the Gemini model.
- **QDRANT_LINK**: URL to your running Qdrant instance.

---

## Notes
- Make sure the `.env` file is created
- If you want to ingest a different document later, repeat the **Ingestion** steps.
- Docker must be running whenever you use the retriever.

---

## Troubleshooting
- If you face module errors, ensure you have activated the correct virtual environment.
- If Docker services fail to start, verify that port `6333` is free.
- Always check your `.env` setup if the API integration doesn't work.

---
DhanyaWad!!!

