from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id= "cvis-tmu/qwen2_5vl-7b-lora-sft-CoT_traineval_1epochs_unifiedformat_groksettings_traininglog",
    task="text-generation",
)

model = ChatHuggingFace(llm= llm)

result= model.invoke("Whats capital of India?")
print(result)