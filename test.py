from langchain_ollama import OllamaLLM

# Connect to your running Ollama server
model = OllamaLLM(model="llama3.2:3b", base_url="http://127.0.0.1:11434")

# Simple test prompt
prompt = "List all fruits in this text: 'Apple, Banana, Mango, Grapes.'"

result = model.invoke(prompt)
print("Model output:", result)
