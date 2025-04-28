from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

import os
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
QDRANT_LINK = os.getenv("QDRANT_LINK")

print("Loading pdf")
loader = PyPDFLoader("../Node_js_docs.pdf")
print("Loaded")
print("chunking the PDF")

pages = loader.load_and_split()
print("chunking done")
split_text = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
print("Splitting the text")
texts = split_text.split_documents(documents=pages)
print("text splitted")

embedder = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GEMINI_API_KEY
    )

print("ingesting the data")
vector_store = QdrantVectorStore.from_documents(
    documents=[],
    collection_name="PDF_DATA",
    url=QDRANT_LINK,
    embedding = embedder
)

vector_store.add_documents(documents=texts)
print("ingestion finished")

