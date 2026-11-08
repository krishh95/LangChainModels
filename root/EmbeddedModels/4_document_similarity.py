from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name = "allegro/herbert-base-cased"
)

data = [
    "The cat is sleeping on the sofa.",
    "A cat is asleep on the couch.",       # similar to the first
    "A dog is running through a park.",
    "The stock market closed higher today."
] 

query = "is couch empty?"


vector_data_embedding = embedding.embed_documents(
    data
)

query_embedding = embedding.embed_query(
    query
)

result = cosine_similarity([query_embedding],vector_data_embedding)[0]

index,score = sorted(
        list(enumerate(result)),
        key= lambda x:x[1]
    )[-1]
print(data[index])
print(f"similarity score is:{score}")


""""
A cat is asleep on the couch.
similarity score is:0.9622102431834272
"""