from huggingface_hub import model_info

repo_id = "Qwen/Qwen3-0.6B"

info = model_info(
    repo_id,
    expand="inferenceProviderMapping"
)

print(info.inference_provider_mapping)