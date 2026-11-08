from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name = "allegro/herbert-base-cased"
)

data = [
    "delhi is capital of india",
    "mumbai is capital of maharashtra",
    "NY is capital for US"
]


result= embedding.embed_documents(
    data
)

print(str(result))