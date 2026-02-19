from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve.server import add_routes
import uvicorn
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="LANGCHAIN SERVER",
    version="1.0",
    description="A simple API server via FASTAPI"
)

# Route for OpenAI model
add_routes(app, ChatOpenAI(), path="/openai")

# Define models
model = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model="mistralai/mistral-7b-instruct",
    temperature=0.7
)
llm = Ollama(model="llama2")

# Define prompts
prompt1 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("user", "Write an essay in 50 words for the given {input}")
])

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("user", "Write a poem in 50 words for the given {input}")
])

# Add routes for essay and poem
add_routes(app, prompt1 | model, path="/essay")
add_routes(app, prompt2 | llm, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
