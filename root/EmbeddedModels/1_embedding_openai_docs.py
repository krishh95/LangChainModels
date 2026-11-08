from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddding = OpenAIEmbeddings(
    model= "text-embedding-3-large",
    dimensions= 32
)
data = [
    "delhi is capital of india",
    "mumbai is capital of maharashtra",
    "NY is capital for US"
]
result = embeddding.embed_documents(data)
print(str(result))