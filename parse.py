from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2:3b", base_url="http://127.0.0.1:11434")

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}."
    "Please follow these instructions carefully: \n\n"
    "1. *Extract Information:* Only extract the information that directly matches the provided description: {parse_description}"
    "2. *No Extra Content:* Do not include any additional text, comments, or explanations in your response. "
    "3. *Empty Response:* If no information matches the description, return an empty string ('')."
    "4. *Direct Data Only:* Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_ollama(dom_content, parse_description):
    """Parse content via Ollama (single batch for speed)"""
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({
        "dom_content": dom_content,
        "parse_description": parse_description
    })
    return response
