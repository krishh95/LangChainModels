from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


model = ChatOpenAI(model="gpt-6-luna")

result = model.invoke("1+2 how much?")

print(result)