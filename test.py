from langchain.llms import OpenAI
import os

#
os.environ["OPENAI_API_KEY"] = "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"
# os.environ["OPENAI_PROXY"] = "http://127.0.0.1:10809"
llm = OpenAI(temperature=0.9)
# llm = OpenAI()
text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))