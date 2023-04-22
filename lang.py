import os 
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 1 calling llms directly  on user input 

# llm = OpenAI(temperature =0.9)
# text = "What would be a good company name for a company that makes colorful socks?"
# print(llm(text))

def generate_text(text):
    llm = OpenAI(temperature =0.9)
    return llm(text)

#2 taking user input and contsucting a prompt from it and then formatting the prompt . we use PromptTemplate

# prompt = PromptTemplate(
#     input_variables=["product"],
#     template="What is a good name for a company that makes {product}?",
# )
# print(prompt.format(product="colorful socks"))

def generate_prompt(product):
    prompt = PromptTemplate(input_variables=["product"], template="What is a good name for a company that makes {product}?")
    return prompt.format(product=product)


#3 chains : combine LLMs and PromptTemplate in multi-steps workflow
# llm = OpenAI(temperature = 0.9)

# prompt = PromptTemplate(
#     input_variables = ["product"],
#     template = "What is a good name for a company that makes {product}?"
# )

# chain =LLMChain(llm,prompt=prompt)

# #run the chain
# chain.run("colorful socks")

def generate_chain(product):
    llm =OpenAI(temperature=0.9)
    prompt = PromptTemplate(input_variables=["product"], template="What is a good name for a company that makes {product}?")
    chain =LLMChain(llm,prompt=prompt)
    return chain.run(product)
