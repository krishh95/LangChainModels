from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name = "allegro/herbert-base-cased"
)

text= "delhi is capital of india"
result= embedding.embed_query(
    text
)

print(str(result))