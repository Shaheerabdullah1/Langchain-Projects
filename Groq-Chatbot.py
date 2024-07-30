from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate


llm = ChatGroq(groq_api_key= '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' , model='Llama3-8b-8192')

System = "You are a intelligent Python Programmer named as Shaheer Abdullah."


Human = "{text}"

prompt= ChatPromptTemplate.from_messages([
    ('system',System),
    ('human',Human)    

])

chain = prompt | llm
user_query=input("Enter the Query: ")
response = chain.invoke({"text":user_query})

print(response.content)










