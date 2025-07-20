# Load local model (e.g. Mistral or LLaMA)
# local_model_loader.py
# This file loads the local language model and generates responses to prompts.

# Version 1: Using Ollama as the local backend (easiest to test)

import subprocess

MODEL_NAME = "mistral"  # Change to the model you have (e.g., "llama3", "gemma", etc.)

def load_model():
    """
    Dummy loader for compatibility. Ollama models run as a background service.
    """
    print(f"Using local model via Ollama: {MODEL_NAME}")
    return MODEL_NAME

def generate_response(model, prompt):
    """
    Uses subprocess to send prompt to the local Ollama model.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output = result.stdout.decode("utf-8").strip()

        # Optional: clean response if Ollama returns extra metadata
        return clean_output(output)

    except Exception as e:
        return f"Error generating response: {e}"

def clean_output(output):
    """
    Optional: remove model tags or streaming artifacts.
    """
    if "[/INST]" in output:
        output = output.split("[/INST]")[-1].strip()
    return output
