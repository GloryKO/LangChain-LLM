import os 
#os.environ["OPENAI_API_KEY"] = os.environ["OPENAI_API_KEY"]
#import langchain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

#calling llms directly  on user input 
llm = openAI(temperature =0.9)
text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))

#taking user input and contsucting a prompt from it and then formatting the prompt . we use PromptTemplate
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
print(prompt.format(product="colorful socks"))

#chains : combine LLMs and PromptTemplate in multi-steps workflow



