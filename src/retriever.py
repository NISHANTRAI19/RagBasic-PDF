from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from embedder import embedder
from google import genai
from google.genai import types

import os
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

QDRANT_LINK = os.getenv("QDRANT_LINK")


retriever = QdrantVectorStore.from_existing_collection(
    url=QDRANT_LINK,
    collection_name="PDF_DATA",
    embedding = embedder
)
search_result = retriever.similarity_search(
    query="what is Node?"
)



client = genai.Client(api_key=GEMINI_API_KEY)
history =[]
while True:
    userInput = input("User:") 
    if userInput.lower() == "exit":
        break
    
    search_result = retriever.similarity_search(query=userInput)
    
    SYSTEM_PROMPT = f"""
    You are a helpful AI assistant who responds based on the available context.
    
    Context:
    {search_result}
    """

    history.append(types.UserContent(parts=[types.Part.from_text(text=userInput)]))

    generate_content_config = types.GenerateContentConfig(
            response_mime_type="text/plain",
            system_instruction=types.Content(
            parts=[types.Part.from_text(text=SYSTEM_PROMPT)]
        )
        )
    response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=history,
            config=generate_content_config,)
    print(f"AI: {response.text}")
    history.append(types.ModelContent( parts=[types.Part.from_text(text=response.text)]))

    