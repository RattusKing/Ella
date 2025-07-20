import sys
from backend.local_model_loader import load_model, generate_response
from backend.rag_engine import retrieve_context

# Load the model once
model = load_model()

# Load persona and system prompts
with open("backend/prompts/persona.txt", "r") as f:
    persona = f.read()

with open("backend/prompts/system_prompt.txt", "r") as f:
    system_prompt = f.read()

def run_chat():
    print("Ella is ready. Type 'exit' to quit.\n")
    chat_history = []

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Ella: Talk to you soon. Stay steady.")
            break

        # Retrieve relevant context from documents
        context = retrieve_context(user_input)

        # Format prompt for the model
        prompt = f"""{system_prompt}

{persona}

[Previous conversation:]
{format_history(chat_history)}

[User says:]
{user_input}

[Contextual info:]
{context}

[Your reply as Ella]:"""

        # Generate Ella's response
        response = generate_response(model, prompt)
        print(f"Ella: {response.strip()}")

        # Update history
        chat_history.append({"user": user_input, "ella": response.strip()})

def format_history(history):
    return "\n".join([f"User: {turn['user']}\nElla: {turn['ella']}" for turn in history[-5:]])

if __name__ == "__main__":
    run_chat()
# Core chatbot logic goes here
