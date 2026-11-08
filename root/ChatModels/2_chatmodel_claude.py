from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()


model = ChatAnthropic(model="claude-sonnet-5")

result = model.invoke("1+2 how much?")

print(result)