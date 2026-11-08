from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddding = OpenAIEmbeddings(
    model= "text-embedding-3-large",
    dimensions= 32
)

result = embeddding.embed_query("delhi is capital of india")
print(str(result))